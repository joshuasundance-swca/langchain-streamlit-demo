import os
from datetime import datetime
from tempfile import NamedTemporaryFile
from typing import Union

import anthropic
import langsmith.utils
import openai
import streamlit as st
from langchain import LLMChain
from langchain.callbacks import StreamlitCallbackHandler
from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks.tracers.langchain import LangChainTracer, wait_for_all_tracers
from langchain.callbacks.tracers.run_collector import RunCollectorCallbackHandler
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI, ChatAnyscale, ChatAnthropic
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory, StreamlitChatMessageHistory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.retriever import BaseRetriever
from langchain.schema.runnable import RunnableConfig
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer
from langsmith.client import Client
from streamlit_feedback import streamlit_feedback

__version__ = "0.0.2"

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
    "anonymizer",
    "chain",
    "client",
    "doc_chain",
    "document_chat_chain_type",
    "llm",
    "ls_tracer",
    "retriever",
    "run",
    "run_id",
    "trace_link",
    "use_presidio",
)

st.session_state.anonymizer = (
    st.session_state.anonymizer or PresidioReversibleAnonymizer()
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
OPENAI_API_KEY = PROVIDER_KEY_DICT["OpenAI"]

MIN_CHUNK_SIZE = 1
MAX_CHUNK_SIZE = 10000
DEFAULT_CHUNK_SIZE = 1000

MIN_CHUNK_OVERLAP = 0
MAX_CHUNK_OVERLAP = 10000
DEFAULT_CHUNK_OVERLAP = 0


@st.cache_data
def get_retriever(
    uploaded_file_bytes: bytes,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> BaseRetriever:
    with NamedTemporaryFile() as temp_file:
        temp_file.write(uploaded_file_bytes)
        temp_file.seek(0)

        loader = PyPDFLoader(temp_file.name)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
        texts = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        db = FAISS.from_documents(texts, embeddings)
        return db.as_retriever()


# --- Sidebar ---
sidebar = st.sidebar
with sidebar:
    st.markdown("# Menu")

    model = st.selectbox(
        label="Chat Model",
        options=SUPPORTED_MODELS,
        index=SUPPORTED_MODELS.index(DEFAULT_MODEL),
    )

    provider = MODEL_DICT[model]

    st.session_state.use_presidio = st.checkbox(
        "Experimental Private Mode",
        value=False,
        help="Use Microsoft Presidio to redact PII from chat messages.",
    )

    provider_api_key = PROVIDER_KEY_DICT.get(provider) or st.text_input(
        f"{provider} API key",
        type="password",
    )

    if st.button("Clear message history"):
        STMEMORY.clear()
        st.session_state.trace_link = None
        st.session_state.run_id = None

    # --- Document Chat Options ---
    with st.expander("Document Chat", expanded=False):
        uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

        openai_api_key = (
            provider_api_key
            if provider == "OpenAI"
            else OPENAI_API_KEY
            or st.sidebar.text_input("OpenAI API Key: ", type="password")
        )

        document_chat = st.checkbox(
            "Document Chat",
            value=False,
            help="Uploaded document will provide context for the chat.",
        )

        chunk_size = st.slider(
            label="chunk_size",
            help="Size of each chunk of text",
            min_value=MIN_CHUNK_SIZE,
            max_value=MAX_CHUNK_SIZE,
            value=DEFAULT_CHUNK_SIZE,
        )
        chunk_overlap = st.slider(
            label="chunk_overlap",
            help="Number of characters to overlap between chunks",
            min_value=MIN_CHUNK_OVERLAP,
            max_value=MAX_CHUNK_OVERLAP,
            value=DEFAULT_CHUNK_OVERLAP,
        )

        chain_type_help_root = (
            "https://python.langchain.com/docs/modules/chains/document/"
        )
        chain_type_help_dict = {
            chain_type_name: f"{chain_type_help_root}/{chain_type_name}"
            for chain_type_name in (
                "stuff",
                "refine",
                "map_reduce",
                "map_rerank",
            )
        }

        chain_type_help = "\n".join(
            f"- [{k}]({v})" for k, v in chain_type_help_dict.items()
        )

        document_chat_chain_type = st.selectbox(
            label="Document Chat Chain Type",
            options=["stuff", "refine", "map_reduce", "map_rerank"],
            index=0,
            help=chain_type_help,
            disabled=not document_chat,
        )

        if uploaded_file:
            if openai_api_key:
                st.session_state.retriever = get_retriever(
                    uploaded_file_bytes=uploaded_file.getvalue(),
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                )
            else:
                st.error("Please enter a valid OpenAI API key.", icon="❌")

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
    # --- Document Chat ---
    if st.session_state.retriever:
        # st.session_state.doc_chain = ConversationalRetrievalChain.from_llm(
        #     st.session_state.llm,
        #     st.session_state.retriever,
        #     memory=MEMORY,
        # )

        st.session_state.doc_chain = RetrievalQA.from_chain_type(
            llm=st.session_state.llm,
            chain_type=document_chat_chain_type,
            retriever=st.session_state.retriever,
            memory=MEMORY,
        )

    else:
        # --- Regular Chat ---
        chat_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    system_prompt + "\nIt's currently {time}.",
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{query}"),
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
            inputs = {"query": prompt}
            callbacks = [RUN_COLLECTOR]
            tags = ["Streamlit Chat"]
            return_only_outputs = True

            if st.session_state.ls_tracer:
                callbacks.append(st.session_state.ls_tracer)

            config = RunnableConfig(
                {
                    "callbacks": callbacks,
                    "tags": tags,
                    "return_only_outputs": return_only_outputs,
                },
            )

            use_document_chat = all(
                [
                    document_chat,
                    st.session_state.doc_chain,
                    st.session_state.retriever,
                ],
            )

            try:
                if use_document_chat:
                    st_handler = StreamlitCallbackHandler(st.container())
                    config["callbacks"].append(st_handler)
                    output_key = st.session_state.doc_chain.output_key
                else:
                    message_placeholder = st.empty()
                    stream_handler = StreamHandler(message_placeholder)
                    config["callbacks"].append(stream_handler)
                    output_key = st.session_state.chain.output_key

                _chain = (
                    st.session_state.doc_chain
                    if use_document_chat
                    else st.session_state.chain
                )
                chain = (
                    (
                        {"query": st.session_state.anonymizer.anonymize}
                        | _chain
                        | (
                            lambda ai_message: {
                                output_key: st.session_state.anonymizer.deanonymize(
                                    ai_message[output_key],
                                ),
                            }
                        )
                    )
                    if st.session_state.use_presidio
                    else _chain
                )
                full_response = chain.invoke(prompt, config)[output_key]

                if use_document_chat:
                    st_handler._complete_current_thought()
                    st.markdown(full_response)
                else:
                    message_placeholder.markdown(full_response)
            except (openai.error.AuthenticationError, anthropic.AuthenticationError):
                st.error(
                    f"Please enter a valid {provider} API key.",
                    icon="❌",
                )
                full_response = None
            if full_response:
                # --- Tracing ---
                if st.session_state.client:
                    st.session_state.run = RUN_COLLECTOR.traced_runs[0]
                    st.session_state.run_id = st.session_state.run.id
                    RUN_COLLECTOR.traced_runs = []
                    wait_for_all_tracers()
                    try:
                        st.session_state.trace_link = st.session_state.client.read_run(
                            st.session_state.run_id,
                        ).url
                    except langsmith.utils.LangSmithError:
                        st.session_state.trace_link = None
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
