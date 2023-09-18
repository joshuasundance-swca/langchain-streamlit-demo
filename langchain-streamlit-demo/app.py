import streamlit as st
from langchain.callbacks.tracers.langchain import wait_for_all_tracers
from langchain.callbacks.tracers.run_collector import RunCollectorCallbackHandler
from langchain.schema.runnable import RunnableConfig


from llm_stuff import (
    _DEFAULT_SYSTEM_PROMPT,
    get_memory,
    get_llm_chain,
    StreamHandler,
    feedback_component,
    get_langsmith_client,
)

st.set_page_config(
    page_title="Chat LangSmith",
    page_icon="🦜",
)

# "# Chat🦜🛠️"
# Initialize State
if "trace_link" not in st.session_state:
    st.session_state.trace_link = None
if "run_id" not in st.session_state:
    st.session_state.run_id = None
st.sidebar.markdown(
    """
# Menu
""",
)

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

memory = get_memory()

chain = get_llm_chain(memory, system_prompt)

client = get_langsmith_client()

run_collector = RunCollectorCallbackHandler()


if st.sidebar.button("Clear message history"):
    print("Clearing message history")
    memory.clear()
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

if st.session_state.trace_link:
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
        full_response = chain.invoke({"input": prompt}, config=runnable_config)["text"]
        message_placeholder.markdown(full_response)

        run = run_collector.traced_runs[0]
        run_collector.traced_runs = []
        st.session_state.run_id = run.id
        wait_for_all_tracers()
        url = client.read_run(run.id).url
        st.session_state.trace_link = url


if st.session_state.get("run_id"):
    feedback_component(client)
