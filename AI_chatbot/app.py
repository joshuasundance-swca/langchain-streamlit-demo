from datetime import datetime

import streamlit as st
from langchain import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks.tracers.langchain import wait_for_all_tracers
from langchain.callbacks.tracers.run_collector import RunCollectorCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import StreamlitChatMessageHistory, ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnableConfig
from langsmith import Client
from streamlit_feedback import streamlit_feedback

st.set_page_config(
    page_title="Chat LangSmith",
    page_icon="🦜",
)


def get_llm_chain(system_prompt: str, memory: ConversationBufferMemory) -> LLMChain:
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
    llm = ChatOpenAI(temperature=0.7, streaming=True)
    return LLMChain(prompt=prompt, llm=llm, memory=memory)


client = Client()


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

_DEFAULT_SYSTEM_PROMPT = "You are a helpful chatbot."

system_prompt = st.sidebar.text_area(
    "Custom Instructions",
    _DEFAULT_SYSTEM_PROMPT,
    help="Custom instructions to provide the language model to determine style, personality, etc.",
)
system_prompt = system_prompt.strip().replace("{", "{{").replace("}", "}}")
memory = ConversationBufferMemory(
    chat_memory=StreamlitChatMessageHistory(key="langchain_messages"),
    return_messages=True,
    memory_key="chat_history",
)

chain = get_llm_chain(system_prompt, memory)

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


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


run_collector = RunCollectorCallbackHandler()


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

# Simple feedback section
# Optionally add a thumbs up/down button for feedback
if st.session_state.get("run_id"):
    # feedback = streamlit_feedback(
    #     feedback_type="thumbs",
    #     key=f"feedback_{st.session_state.run_id}",
    # )
    # scores = {"👍": 1, "👎": 0}
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
        st.session_state.feedback = {"feedback_id": str(feedback.id), "score": score}
        st.toast("Feedback recorded!", icon="📝")


# # Prompt for more information, if feedback was submitted
# if st.session_state.get("feedback"):
#     feedback = st.session_state.get("feedback")
#     feedback_id = feedback["feedback_id"]
#     score = feedback["score"]
#     if score == 0:
#         if correction := st.text_input(
#             label="What would the correct or preferred response have been?",
#             key=f"correction_{feedback_id}",
#         ):
#             st.session_state.feedback_update = {
#                 "correction": {"desired": correction},
#                 "feedback_id": feedback_id,
#             }
#     elif score == 1:
#         if comment := st.text_input(
#             label="Anything else you'd like to add about this response?",
#             key=f"comment_{feedback_id}",
#         ):
#             st.session_state.feedback_update = {
#                 "comment": comment,
#                 "feedback_id": feedback_id,
#             }
# # Update the feedback if additional information was provided
# if st.session_state.get("feedback_update"):
#     feedback_update = st.session_state.get("feedback_update")
#     feedback_id = feedback_update.pop("feedback_id")
#     client.update_feedback(feedback_id, **feedback_update)
#     # Clear the comment or correction box
#     _reset_feedback()
