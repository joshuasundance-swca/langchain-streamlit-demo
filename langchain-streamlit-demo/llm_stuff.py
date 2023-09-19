from datetime import datetime

import streamlit as st
from langchain import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI, ChatAnyscale, ChatAnthropic
from langchain.chat_models.base import BaseChatModel
from langchain.memory import ConversationBufferMemory, StreamlitChatMessageHistory
from langchain.memory.chat_memory import BaseChatMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from streamlit_feedback import streamlit_feedback

_DEFAULT_SYSTEM_PROMPT = "You are a helpful chatbot."

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
_DEFAULT_MODEL = "gpt-3.5-turbo"

_DEFAULT_TEMPERATURE = 0.7
_MIN_TEMPERATURE = 0.0
_MAX_TEMPERATURE = 1.0

_DEFAULT_MAX_TOKENS = 1000
_MIN_TOKENS = 1
_MAX_TOKENS = 100000


def get_memory() -> BaseChatMemory:
    return ConversationBufferMemory(
        chat_memory=StreamlitChatMessageHistory(key="langchain_messages"),
        return_messages=True,
        memory_key="chat_history",
    )


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
    memory = get_memory()
    llm = get_llm(model, provider_api_key, temperature, max_tokens)
    return LLMChain(prompt=prompt, llm=llm, memory=memory or get_memory())


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
