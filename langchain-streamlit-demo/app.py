import os
from datetime import datetime
from typing import Union

import anthropic
import openai
import streamlit as st
from langchain import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks.tracers.langchain import wait_for_all_tracers
from langchain.callbacks.tracers.run_collector import RunCollectorCallbackHandler
from langchain.chat_models import ChatOpenAI, ChatAnyscale, ChatAnthropic
from langchain.chat_models.base import BaseChatModel
from langchain.memory import ConversationBufferMemory, StreamlitChatMessageHistory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnableConfig
from langsmith.client import Client
from streamlit_feedback import streamlit_feedback

st.set_page_config(
    page_title="langchain-streamlit-demo",
    page_icon="🦜",
)

st.sidebar.markdown("# Menu")


_STMEMORY = StreamlitChatMessageHistory(key="langchain_messages")
_MEMORY = ConversationBufferMemory(
    chat_memory=_STMEMORY,
    return_messages=True,
    memory_key="chat_history",
)

_DEFAULT_SYSTEM_PROMPT = os.environ.get(
    "DEFAULT_SYSTEM_PROMPT",
    "You are a helpful chatbot.",
)

_MODEL_DICT = {
    "gpt-3.5-turbo": "OpenAI",
    "gpt-4": "OpenAI",
    "claude-instant-v1": "Anthropic",
    "claude-2": "Anthropic",
    "meta-llama/Llama-2-7b-chat-hf": "Anyscale Endpoints",
    "meta-llama/Llama-2-13b-chat-hf": "Anyscale Endpoints",
    "meta-llama/Llama-2-70b-chat-hf": "Anyscale Endpoints",
}
_SUPPORTED_MODELS = list(_MODEL_DICT.keys())
_DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "gpt-3.5-turbo")

_DEFAULT_TEMPERATURE = float(os.environ.get("DEFAULT_TEMPERATURE", 0.7))
_MIN_TEMPERATURE = float(os.environ.get("MIN_TEMPERATURE", 0.0))
_MAX_TEMPERATURE = float(os.environ.get("MAX_TEMPERATURE", 1.0))

_DEFAULT_MAX_TOKENS = int(os.environ.get("DEFAULT_MAX_TOKENS", 1000))
_MIN_TOKENS = int(os.environ.get("MIN_MAX_TOKENS", 1))
_MAX_TOKENS = int(os.environ.get("MAX_MAX_TOKENS", 100000))


def get_llm(
    model: str,
    provider_api_key: str,
    temperature: float,
    max_tokens: int = _DEFAULT_MAX_TOKENS,
) -> BaseChatModel:
    if _MODEL_DICT[model] == "OpenAI":
        return ChatOpenAI(
            model=model,
            openai_api_key=provider_api_key,
            temperature=temperature,
            streaming=True,
            max_tokens=max_tokens,
        )
    elif _MODEL_DICT[model] == "Anthropic":
        return ChatAnthropic(
            model_name=model,
            anthropic_api_key=provider_api_key,
            temperature=temperature,
            streaming=True,
            max_tokens_to_sample=max_tokens,
        )
    elif _MODEL_DICT[model] == "Anyscale Endpoints":
        return ChatAnyscale(
            model=model,
            anyscale_api_key=provider_api_key,
            temperature=temperature,
            streaming=True,
            max_tokens=max_tokens,
        )
    else:
        raise NotImplementedError(f"Unknown model {model}")


def get_llm_chain(
    model: str,
    provider_api_key: str,
    system_prompt: str = _DEFAULT_SYSTEM_PROMPT,
    temperature: float = _DEFAULT_TEMPERATURE,
    max_tokens: int = _DEFAULT_MAX_TOKENS,
) -> LLMChain:
    """Return a basic LLMChain with memory."""
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt + "\nIt's currently {time}.",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ],
    ).partial(time=lambda: str(datetime.now()))
    llm = get_llm(model, provider_api_key, temperature, max_tokens)
    return LLMChain(prompt=prompt, llm=llm, memory=_MEMORY)


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


def feedback_component(client):
    scores = {"😀": 1, "🙂": 0.75, "😐": 0.5, "🙁": 0.25, "😞": 0}
    if feedback := streamlit_feedback(
        feedback_type="faces",
        optional_text_label="[Optional] Please provide an explanation",
        key=f"feedback_{st.session_state.run_id}",
    ):
        score = scores[feedback["score"]]
        feedback = client.create_feedback(
            st.session_state.run_id,
            feedback["type"],
            score=score,
            comment=feedback.get("text", None),
        )
        st.session_state.feedback = {"feedback_id": str(feedback.id), "score": score}
        st.toast("Feedback recorded!", icon="📝")


# Initialize State
if "trace_link" not in st.session_state:
    st.session_state.trace_link = None
if "run_id" not in st.session_state:
    st.session_state.run_id = None
if len(_STMEMORY.messages) == 0:
    _STMEMORY.add_ai_message("Hello! I'm a helpful AI chatbot. Ask me a question!")

for msg in _STMEMORY.messages:
    st.chat_message(
        msg.type,
        avatar="🦜" if msg.type in ("ai", "assistant") else None,
    ).write(msg.content)

model = st.sidebar.selectbox(
    label="Chat Model",
    options=_SUPPORTED_MODELS,
    index=_SUPPORTED_MODELS.index(_DEFAULT_MODEL),
)
provider = _MODEL_DICT[model]


def api_key_from_env(_provider: str) -> Union[str, None]:
    if _provider == "OpenAI":
        return os.environ.get("OPENAI_API_KEY")
    elif _provider == "Anthropic":
        return os.environ.get("ANTHROPIC_API_KEY")
    elif _provider == "Anyscale Endpoints":
        return os.environ.get("ANYSCALE_API_KEY")
    elif _provider == "LANGSMITH":
        return os.environ.get("LANGCHAIN_API_KEY")
    else:
        return None


provider_api_key = api_key_from_env(provider) or st.sidebar.text_input(
    f"{provider} API key",
    type="password",
)
langsmith_api_key = api_key_from_env("LANGSMITH") or st.sidebar.text_input(
    "LangSmith API Key (optional)",
    type="password",
)
if langsmith_api_key:
    langsmith_project = os.environ.get("LANGCHAIN_PROJECT") or st.sidebar.text_input(
        "LangSmith Project Name",
        value="langchain-streamlit-demo",
    )
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = langsmith_project

    client = Client(api_key=langsmith_api_key)
else:
    langsmith_project = None
    client = None

system_prompt = (
    st.sidebar.text_area(
        "Custom Instructions",
        _DEFAULT_SYSTEM_PROMPT,
        help="Custom instructions to provide the language model to determine style, personality, etc.",
    )
    .strip()
    .replace("{", "{{")
    .replace("}", "}}")
)

if st.sidebar.button("Clear message history"):
    print("Clearing message history")
    _STMEMORY.clear()
    st.session_state.trace_link = None
    st.session_state.run_id = None

temperature = st.sidebar.slider(
    "Temperature",
    min_value=_MIN_TEMPERATURE,
    max_value=_MAX_TEMPERATURE,
    value=_DEFAULT_TEMPERATURE,
    help="Higher values give more random results.",
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    min_value=_MIN_TOKENS,
    max_value=_MAX_TOKENS,
    value=_DEFAULT_MAX_TOKENS,
    help="Higher values give longer results.",
)
chain = None
if provider_api_key:
    chain = get_llm_chain(
        model,
        provider_api_key,
        system_prompt,
        temperature,
        max_tokens,
    )

run_collector = RunCollectorCallbackHandler()


def _reset_feedback():
    st.session_state.feedback_update = None
    st.session_state.feedback = None


if chain:
    prompt = st.chat_input(placeholder="Ask me a question!")
    if prompt:
        st.chat_message("user").write(prompt)
        _reset_feedback()

        with st.chat_message("assistant", avatar="🦜"):
            message_placeholder = st.empty()
            stream_handler = StreamHandler(message_placeholder)
            runnable_config = RunnableConfig(
                callbacks=[run_collector, stream_handler],
                tags=["Streamlit Chat"],
            )
            try:
                full_response = chain.invoke(
                    {"input": prompt},
                    config=runnable_config,
                )["text"]
            except (openai.error.AuthenticationError, anthropic.AuthenticationError):
                st.error(f"Please enter a valid {provider} API key.", icon="❌")
                st.stop()
            message_placeholder.markdown(full_response)

            if client:
                run = run_collector.traced_runs[0]
                run_collector.traced_runs = []
                st.session_state.run_id = run.id
                wait_for_all_tracers()
                url = client.read_run(run.id).url
                st.session_state.trace_link = url
    if client and st.session_state.get("run_id"):
        feedback_component(client)

else:
    st.error(f"Please enter a valid {provider} API key.", icon="❌")

if client and st.session_state.get("trace_link"):
    st.sidebar.markdown(
        f'<a href="{st.session_state.trace_link}" target="_blank"><button>Latest Trace: 🛠️</button></a>',
        unsafe_allow_html=True,
    )
