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
from langchain.memory import ConversationBufferMemory, StreamlitChatMessageHistory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnableConfig
from langsmith.client import Client
from streamlit_feedback import streamlit_feedback

# --- Initialization ---
st.set_page_config(
    page_title="langchain-streamlit-demo",
    page_icon="🦜",
)


def st_init_null(*variable_names) -> None:
    for variable_name in variable_names:
        if variable_name not in st.session_state:
            st.session_state[variable_name] = None


st_init_null(
    "trace_link",
    "run_id",
    "model",
    "provider",
    "system_prompt",
    "llm",
    "chain",
    "retriever",
    "client",
)

# --- Memory ---
_STMEMORY = StreamlitChatMessageHistory(key="langchain_messages")
_MEMORY = ConversationBufferMemory(
    chat_memory=_STMEMORY,
    return_messages=True,
    memory_key="chat_history",
)


# --- Callbacks ---
class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


st.session_state.run_collector = RunCollectorCallbackHandler()


# --- Model Selection Helpers ---
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


def api_key_from_env(provider_name: str) -> Union[str, None]:
    if provider_name == "OpenAI":
        return os.environ.get("OPENAI_API_KEY")
    elif provider_name == "Anthropic":
        return os.environ.get("ANTHROPIC_API_KEY")
    elif provider_name == "Anyscale Endpoints":
        return os.environ.get("ANYSCALE_API_KEY")
    elif provider_name == "LANGSMITH":
        return os.environ.get("LANGCHAIN_API_KEY")
    else:
        return None


# --- Sidebar ---
sidebar = st.sidebar
with sidebar:
    st.markdown("# Menu")

    st.session_state.model = st.selectbox(
        label="Chat Model",
        options=_SUPPORTED_MODELS,
        index=_SUPPORTED_MODELS.index(
            st.session_state.model
            or os.environ.get("DEFAULT_MODEL")
            or "gpt-3.5-turbo",
        ),
    )

    # document_chat = st.checkbox(
    #     "Document Chat",
    #     value=False,
    #     help="Upload a document",
    # )

    if st.button("Clear message history"):
        _STMEMORY.clear()
        st.session_state.trace_link = None
        st.session_state.run_id = None

    # --- Advanced Options ---
    with st.expander("Advanced Options", expanded=False):
        st.session_state.system_prompt = (
            st.text_area(
                "Custom Instructions",
                st.session_state.system_prompt
                or os.environ.get("DEFAULT_SYSTEM_PROMPT")
                or "You are a helpful chatbot.",
                help="Custom instructions to provide the language model to determine style, personality, etc.",
            )
            .strip()
            .replace("{", "{{")
            .replace("}", "}}")
        )

        temperature = st.slider(
            "Temperature",
            min_value=float(os.environ.get("MIN_TEMPERATURE", 0.0)),
            max_value=float(os.environ.get("MIN_TEMPERATURE", 1.0)),
            value=float(os.environ.get("DEFAULT_TEMPERATURE", 0.7)),
            help="Higher values give more random results.",
        )

        max_tokens = st.slider(
            "Max Tokens",
            min_value=int(os.environ.get("MIN_MAX_TOKENS", 1)),
            max_value=int(os.environ.get("MAX_MAX_TOKENS", 100000)),
            value=int(os.environ.get("DEFAULT_MAX_TOKENS", 1000)),
            help="Higher values give longer results.",
        )

        # --- API Keys ---
        st.session_state.provider = _MODEL_DICT[st.session_state.model]

        provider_api_key = st.text_input(
            f"{st.session_state.provider} API key",
            value=api_key_from_env(st.session_state.provider) or "",
            type="password",
        )

        langsmith_api_key = st.text_input(
            "LangSmith API Key (optional)",
            value=api_key_from_env("LANGSMITH") or "",
            type="password",
        )
        langsmith_project = st.text_input(
            "LangSmith Project Name",
            value=os.environ.get("LANGCHAIN_PROJECT") or "langchain-streamlit-demo",
        )
        if langsmith_api_key:
            os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
            os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key
            os.environ["LANGCHAIN_TRACING_V2"] = "true"
            os.environ["LANGCHAIN_PROJECT"] = langsmith_project
            client = Client(api_key=langsmith_api_key)


# --- LLM Instantiation ---
if provider_api_key:
    if st.session_state.provider == "OpenAI":
        llm = ChatOpenAI(
            model=st.session_state.model,
            openai_api_key=provider_api_key,
            temperature=temperature,
            streaming=True,
            max_tokens=max_tokens,
        )
    elif st.session_state.provider == "Anthropic":
        llm = ChatAnthropic(
            model_name=st.session_state.model,
            anthropic_api_key=provider_api_key,
            temperature=temperature,
            streaming=True,
            max_tokens_to_sample=max_tokens,
        )
    elif st.session_state.provider == "Anyscale Endpoints":
        llm = ChatAnyscale(
            model=st.session_state.model,
            anyscale_api_key=provider_api_key,
            temperature=temperature,
            streaming=True,
            max_tokens=max_tokens,
        )


# --- Chat History ---
if len(_STMEMORY.messages) == 0:
    _STMEMORY.add_ai_message("Hello! I'm a helpful AI chatbot. Ask me a question!")

for msg in _STMEMORY.messages:
    st.chat_message(
        msg.type,
        avatar="🦜" if msg.type in ("ai", "assistant") else None,
    ).write(msg.content)


# --- Current Chat ---
if st.session_state.llm:
    # if isinstance(retriever, BaseRetriever):
    #     # --- Document Chat ---
    #     chain = ConversationalRetrievalChain.from_llm(
    #         llm,
    #         retriever,
    #         memory=_MEMORY,
    #     )
    # else:
    # --- Regular Chat ---
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                st.session_state.system_prompt + "\nIt's currently {time}.",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ],
    ).partial(time=lambda: str(datetime.now()))
    st.session_state.chain = LLMChain(
        prompt=prompt,
        llm=st.session_state.llm,
        memory=_MEMORY,
    )

    # --- Chat Input ---
    prompt = st.chat_input(placeholder="Ask me a question!")
    if prompt:
        st.chat_message("user").write(prompt)
        st.session_state.feedback_update = None
        st.session_state.feedback = None

        # --- Chat Output ---
        with st.chat_message("assistant", avatar="🦜"):
            message_placeholder = st.empty()
            stream_handler = StreamHandler(message_placeholder)
            runnable_config = RunnableConfig(
                callbacks=[st.session_state.run_collector, stream_handler],
                tags=["Streamlit Chat"],
            )
            try:
                full_response = st.session_state.chain.invoke(
                    {"input": prompt},
                    config=runnable_config,
                )["text"]
            except (openai.error.AuthenticationError, anthropic.AuthenticationError):
                st.error(
                    f"Please enter a valid {st.session_state.provider} API key.",
                    icon="❌",
                )
                st.stop()
            message_placeholder.markdown(full_response)

            # --- Tracing ---
            if client:
                run = st.session_state.run_collector.traced_runs[0]
                st.session_state.run_collector.traced_runs = []
                st.session_state.run_id = run.id
                wait_for_all_tracers()
                url = client.read_run(run.id).url
                st.session_state.trace_link = url
                with sidebar:
                    st.markdown(
                        f'<a href="{st.session_state.trace_link}" target="_blank"><button>Latest Trace: 🛠️</button></a>',
                        unsafe_allow_html=True,
                    )

    # --- Feedback ---
    if client and st.session_state.get("run_id"):
        scores = {"😀": 1, "🙂": 0.75, "😐": 0.5, "🙁": 0.25, "😞": 0}
        feedback = streamlit_feedback(
            feedback_type="faces",
            optional_text_label="[Optional] Please provide an explanation",
            key=f"feedback_{st.session_state.run_id}",
        )
        if feedback:
            score = scores[feedback["score"]]
            feedback = client.create_feedback(
                st.session_state.run_id,
                feedback["type"],
                score=score,
                comment=feedback.get("text", None),
            )
            st.session_state.feedback = {
                "feedback_id": str(feedback.id),
                "score": score,
            }
            st.toast("Feedback recorded!", icon="📝")

else:
    st.error(f"Please enter a valid {st.session_state.provider} API key.", icon="❌")
