import os

import anthropic
import openai
import streamlit as st
from langchain.callbacks.manager import tracing_v2_enabled
from langchain.callbacks.tracers.langchain import wait_for_all_tracers
from langchain.callbacks.tracers.run_collector import RunCollectorCallbackHandler
from langchain.schema.runnable import RunnableConfig
from langsmith.client import Client

from llm_stuff import (
    _DEFAULT_SYSTEM_PROMPT,
    get_llm_chain,
    StreamHandler,
    feedback_component,
)

st.set_page_config(
    page_title="langchain-streamlit-demo",
    page_icon="🦜",
)

# Initialize State
if "trace_link" not in st.session_state:
    st.session_state.trace_link = None
if "run_id" not in st.session_state:
    st.session_state.run_id = None

st.sidebar.markdown("# Menu")
models = [
    "gpt-3.5-turbo",
    "gpt-4",
    "claude-instant-v1",
    "claude-2",
    "meta-llama/Llama-2-7b-chat-hf",
    "meta-llama/Llama-2-13b-chat-hf",
    "meta-llama/Llama-2-70b-chat-hf",
]
model = st.sidebar.selectbox(label="Chat Model", options=models, index=0)

if model.startswith("gpt"):
    provider = "OpenAI"
elif model.startswith("claude"):
    provider = "Anthropic"
elif model.startswith("meta-llama"):
    provider = "Anyscale"
else:
    st.stop()

if not model:
    st.error("Please select a model and provide an API key.", icon="❌")
    st.stop()

provider_api_key = st.sidebar.text_input(f"{provider} API key", type="password")

langsmith_api_key = st.sidebar.text_input(
    "LangSmith API Key (optional)",
    type="password",
)

if langsmith_api_key.startswith("ls__"):
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

if provider_api_key:
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
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        help="Higher values give more random results.",
    )

    chain = get_llm_chain(model, provider_api_key, system_prompt, temperature)

    run_collector = RunCollectorCallbackHandler()

    if st.sidebar.button("Clear message history"):
        print("Clearing message history")
        chain.memory.clear()
        st.session_state.trace_link = None
        st.session_state.run_id = None

    # Display chat messages from history on app rerun
    # NOTE: This won't be necessary for Streamlit 1.26+, you can just pass the type directly
    # https://github.com/streamlit/streamlit/pull/7094
    def _get_openai_type(msg):
        if msg.type == "human":
            return "user"
        if msg.type == "ai":
            return "assistant"
        return msg.role if msg.type == "chat" else msg.type

    for msg in st.session_state.langchain_messages:
        streamlit_type = _get_openai_type(msg)
        avatar = "🦜" if streamlit_type == "assistant" else None
        with st.chat_message(streamlit_type, avatar=avatar):
            st.markdown(msg.content)

    if client and st.session_state.trace_link:
        st.sidebar.markdown(
            f'<a href="{st.session_state.trace_link}" target="_blank"><button>Latest Trace: 🛠️</button></a>',
            unsafe_allow_html=True,
        )

    def _reset_feedback():
        st.session_state.feedback_update = None
        st.session_state.feedback = None

    if prompt := st.chat_input(placeholder="Ask me a question!"):
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
                if client and langsmith_project:
                    with tracing_v2_enabled(project_name=langsmith_project):
                        full_response = chain.invoke(
                            {"input": prompt},
                            config=runnable_config,
                        )["text"]
                else:
                    full_response = chain.invoke(
                        {"input": prompt},
                        config=runnable_config,
                    )["text"]
            except (openai.error.AuthenticationError, anthropic.AuthenticationError):
                st.error("Please enter a valid {provider} API key.", icon="❌")
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
    st.stop()
