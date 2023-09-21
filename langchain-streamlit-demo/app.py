import os
from datetime import datetime
from typing import Union

import anthropic
import openai
import streamlit as st
from langchain import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks.tracers.langchain import LangChainTracer, wait_for_all_tracers
from langchain.callbacks.tracers.run_collector import RunCollectorCallbackHandler
from langchain.chat_models import ChatOpenAI, ChatAnyscale, ChatAnthropic
from langchain.memory import ConversationBufferMemory, StreamlitChatMessageHistory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
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
    "chain",
    "client",
    "llm",
    "ls_tracer",
    "run",
    "run_id",
    "trace_link",
)

# --- Memory ---
STMEMORY = StreamlitChatMessageHistory(key="langchain_messages")
MEMORY = ConversationBufferMemory(
    chat_memory=STMEMORY,
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


RUN_COLLECTOR = RunCollectorCallbackHandler()


# --- Model Selection Helpers ---
MODEL_DICT = {
    "gpt-3.5-turbo": "OpenAI",
    "gpt-4": "OpenAI",
    "claude-instant-v1": "Anthropic",
    "claude-2": "Anthropic",
    "meta-llama/Llama-2-7b-chat-hf": "Anyscale Endpoints",
    "meta-llama/Llama-2-13b-chat-hf": "Anyscale Endpoints",
    "meta-llama/Llama-2-70b-chat-hf": "Anyscale Endpoints",
}
SUPPORTED_MODELS = list(MODEL_DICT.keys())


# --- Constants from Environment Variables ---
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "gpt-3.5-turbo")
DEFAULT_SYSTEM_PROMPT = os.environ.get(
    "DEFAULT_SYSTEM_PROMPT",
    "You are a helpful chatbot.",
)
MIN_TEMP = float(os.environ.get("MIN_TEMPERATURE", 0.0))
MAX_TEMP = float(os.environ.get("MAX_TEMPERATURE", 1.0))
DEFAULT_TEMP = float(os.environ.get("DEFAULT_TEMPERATURE", 0.7))
MIN_MAX_TOKENS = int(os.environ.get("MIN_MAX_TOKENS", 1))
MAX_MAX_TOKENS = int(os.environ.get("MAX_MAX_TOKENS", 100000))
DEFAULT_MAX_TOKENS = int(os.environ.get("DEFAULT_MAX_TOKENS", 1000))
DEFAULT_LANGSMITH_PROJECT = os.environ.get("LANGCHAIN_PROJECT")
PROVIDER_KEY_DICT = {
    "OpenAI": os.environ.get("OPENAI_API_KEY", ""),
    "Anthropic": os.environ.get("ANTHROPIC_API_KEY", ""),
    "Anyscale Endpoints": os.environ.get("ANYSCALE_API_KEY", ""),
    "LANGSMITH": os.environ.get("LANGCHAIN_API_KEY", ""),
}


# --- Sidebar ---
sidebar = st.sidebar
with sidebar:
    st.markdown("# Menu")

    model = st.selectbox(
        label="Chat Model",
        options=SUPPORTED_MODELS,
        index=SUPPORTED_MODELS.index(DEFAULT_MODEL),
    )

    # document_chat = st.checkbox(
    #     "Document Chat",
    #     value=False,
    #     help="Upload a document",
    # )

    if st.button("Clear message history"):
        STMEMORY.clear()
        st.session_state.trace_link = None
        st.session_state.run_id = None

    # --- Advanced Options ---
    with st.expander("Advanced Options", expanded=False):
        st.markdown("## Feedback Scale")
        use_faces = st.toggle(label="`Thumbs` ⇄ `Faces`", value=False)
        feedback_option = "faces" if use_faces else "thumbs"

        system_prompt = (
            st.text_area(
                "Custom Instructions",
                DEFAULT_SYSTEM_PROMPT,
                help="Custom instructions to provide the language model to determine style, personality, etc.",
            )
            .strip()
            .replace("{", "{{")
            .replace("}", "}}")
        )
        temperature = st.slider(
            "Temperature",
            min_value=MIN_TEMP,
            max_value=MAX_TEMP,
            value=DEFAULT_TEMP,
            help="Higher values give more random results.",
        )

        max_tokens = st.slider(
            "Max Tokens",
            min_value=MIN_MAX_TOKENS,
            max_value=MAX_MAX_TOKENS,
            value=DEFAULT_MAX_TOKENS,
            help="Higher values give longer results.",
        )

        # --- API Keys ---
        provider = MODEL_DICT[model]

        provider_api_key = PROVIDER_KEY_DICT.get(provider) or st.text_input(
            f"{provider} API key",
            type="password",
        )

        LANGSMITH_API_KEY = PROVIDER_KEY_DICT.get("LANGSMITH") or st.text_input(
            "LangSmith API Key (optional)",
            type="password",
        )
        LANGSMITH_PROJECT = DEFAULT_LANGSMITH_PROJECT or st.text_input(
            "LangSmith Project Name",
            value="langchain-streamlit-demo",
        )
        if st.session_state.client is None and LANGSMITH_API_KEY:
            st.session_state.client = Client(
                api_url="https://api.smith.langchain.com",
                api_key=LANGSMITH_API_KEY,
            )
            st.session_state.ls_tracer = LangChainTracer(
                project_name=LANGSMITH_PROJECT,
                client=st.session_state.client,
            )


# --- LLM Instantiation ---
if provider_api_key:
    if provider == "OpenAI":
        st.session_state.llm = ChatOpenAI(
            model=model,
            openai_api_key=provider_api_key,
            temperature=temperature,
            streaming=True,
            max_tokens=max_tokens,
        )
    elif provider == "Anthropic":
        st.session_state.llm = ChatAnthropic(
            model_name=model,
            anthropic_api_key=provider_api_key,
            temperature=temperature,
            streaming=True,
            max_tokens_to_sample=max_tokens,
        )
    elif provider == "Anyscale Endpoints":
        st.session_state.llm = ChatAnyscale(
            model=model,
            anyscale_api_key=provider_api_key,
            temperature=temperature,
            streaming=True,
            max_tokens=max_tokens,
        )


# --- Chat History ---
if len(STMEMORY.messages) == 0:
    STMEMORY.add_ai_message("Hello! I'm a helpful AI chatbot. Ask me a question!")

for msg in STMEMORY.messages:
    st.chat_message(
        msg.type,
        avatar="🦜" if msg.type in ("ai", "assistant") else None,
    ).write(msg.content)


# --- Current Chat ---
if st.session_state.llm:
    # if isinstance(retriever, BaseRetriever):
    #     # --- Document Chat ---
    #     chain = ConversationalRetrievalChain.from_llm(
    #         st.session_state.llm,
    #         retriever,
    #         memory=_MEMORY,
    #     )
    # else:
    # --- Regular Chat ---
    chat_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt + "\nIt's currently {time}.",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ],
    ).partial(time=lambda: str(datetime.now()))
    st.session_state.chain = LLMChain(
        prompt=chat_prompt,
        llm=st.session_state.llm,
        memory=MEMORY,
    )

    # --- Chat Input ---
    prompt = st.chat_input(placeholder="Ask me a question!")
    if prompt:
        st.chat_message("user").write(prompt)
        feedback_update = None
        feedback = None

        # --- Chat Output ---
        with st.chat_message("assistant", avatar="🦜"):
            message_placeholder = st.empty()
            stream_handler = StreamHandler(message_placeholder)
            callbacks = [RUN_COLLECTOR, stream_handler]
            if st.session_state.ls_tracer:
                callbacks.append(st.session_state.ls_tracer)

            try:
                full_response = st.session_state.chain(
                    {"input": prompt},
                    callbacks=callbacks,
                    tags=["Streamlit Chat"],
                )["text"]
            except (openai.error.AuthenticationError, anthropic.AuthenticationError):
                st.error(
                    f"Please enter a valid {provider} API key.",
                    icon="❌",
                )
                full_response = None
            if full_response:
                message_placeholder.markdown(full_response)

                # --- Tracing ---
                if st.session_state.client:
                    st.session_state.run = RUN_COLLECTOR.traced_runs[0]
                    st.session_state.run_id = st.session_state.run.id
                    RUN_COLLECTOR.traced_runs = []
                    wait_for_all_tracers()
                    st.session_state.trace_link = st.session_state.client.read_run(
                        st.session_state.run_id,
                    ).url
    if st.session_state.trace_link:
        with sidebar:
            st.markdown(
                f'<a href="{st.session_state.trace_link}" target="_blank"><button>Latest Trace: 🛠️</button></a>',
                unsafe_allow_html=True,
            )

    # --- Feedback ---
    if st.session_state.client and st.session_state.run_id:
        feedback = streamlit_feedback(
            feedback_type=feedback_option,
            optional_text_label="[Optional] Please provide an explanation",
            key=f"feedback_{st.session_state.run_id}",
        )

        # Define score mappings for both "thumbs" and "faces" feedback systems
        score_mappings: dict[str, dict[str, Union[int, float]]] = {
            "thumbs": {"👍": 1, "👎": 0},
            "faces": {"😀": 1, "🙂": 0.75, "😐": 0.5, "🙁": 0.25, "😞": 0},
        }

        # Get the score mapping based on the selected feedback option
        scores = score_mappings[feedback_option]

        if feedback:
            # Get the score from the selected feedback option's score mapping
            score = scores.get(
                feedback["score"],
            )

            if score is not None:
                # Formulate feedback type string incorporating the feedback option
                # and score value
                feedback_type_str = f"{feedback_option} {feedback['score']}"

                # Record the feedback with the formulated feedback type string
                # and optional comment
                feedback_record = st.session_state.client.create_feedback(
                    st.session_state.run_id,
                    feedback_type_str,
                    score=score,
                    comment=feedback.get("text"),
                )
                # feedback = {
                #     "feedback_id": str(feedback_record.id),
                #     "score": score,
                # }
                st.toast("Feedback recorded!", icon="📝")
            else:
                st.warning("Invalid feedback score.")

else:
    st.error(f"Please enter a valid {provider} API key.", icon="❌")
