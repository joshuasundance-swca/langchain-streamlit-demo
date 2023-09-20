import os

import anthropic
import openai
import streamlit as st
from langchain.callbacks.tracers.langchain import wait_for_all_tracers
from langchain.callbacks.tracers.run_collector import RunCollectorCallbackHandler
from langchain.schema.runnable import RunnableConfig
from langsmith.client import Client

from llm_stuff import (
    _MEMORY,
    _MODEL_DICT,
    _SUPPORTED_MODELS,
    _DEFAULT_MODEL,
    _DEFAULT_SYSTEM_PROMPT,
    _DEFAULT_TEMPERATURE,
    _MIN_TEMPERATURE,
    _MAX_TEMPERATURE,
    _DEFAULT_MAX_TOKENS,
    _MIN_TOKENS,
    _MAX_TOKENS,
    get_llm_chain,
    StreamHandler,
    feedback_component,
)

st.set_page_config(
    page_title="langchain-streamlit-demo",
    page_icon="🦜",
)

st.sidebar.markdown("# Menu")

# Initialize State
if "trace_link" not in st.session_state:
    st.session_state.trace_link = None
if "run_id" not in st.session_state:
    st.session_state.run_id = None

model = st.sidebar.selectbox(
    label="Chat Model",
    options=_SUPPORTED_MODELS,
    index=_SUPPORTED_MODELS.index(_DEFAULT_MODEL),
)
provider = _MODEL_DICT[model]

provider_api_key = st.sidebar.text_input(f"{provider} API key", type="password")
langsmith_api_key = st.sidebar.text_input(
    "LangSmith API Key (optional)",
    type="password",
)
if langsmith_api_key:
    langsmith_project = st.sidebar.text_input(
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

if st.sidebar.button("Clear message history"):
    print("Clearing message history")
    st.session_state["langchain_messages"].memory.clear()
    st.session_state.trace_link = None
    st.session_state.run_id = None

for msg in _MEMORY.messages:
    with st.chat_message(
        msg.type,
        avatar="🦜" if msg.type in ("ai", "assistant") else None,
    ):
        st.markdown(msg.content)


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
    if client and st.session_state.run_id:
        feedback_component(client)

else:
    st.error(f"Please enter a valid {provider} API key.", icon="❌")

if client and st.session_state.trace_link:
    st.sidebar.markdown(
        f'<a href="{st.session_state.trace_link}" target="_blank"><button>Latest Trace: 🛠️</button></a>',
        unsafe_allow_html=True,
    )
