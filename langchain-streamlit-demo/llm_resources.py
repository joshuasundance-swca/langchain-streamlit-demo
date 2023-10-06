from tempfile import NamedTemporaryFile
from typing import Tuple, List, Optional, Dict

from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import RetrievalQA, LLMChain
from langchain.chat_models import (
    AzureChatOpenAI,
    ChatOpenAI,
    ChatAnthropic,
    ChatAnyscale,
)
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.schema import Document, BaseRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

from defaults import DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP, DEFAULT_RETRIEVER_K
from qagen import get_rag_qa_gen_chain
from summarize import get_rag_summarization_chain


def get_runnable(
    use_document_chat: bool,
    document_chat_chain_type: str,
    llm,
    retriever,
    memory,
    chat_prompt,
    summarization_prompt,
):
    if not use_document_chat:
        return LLMChain(
            prompt=chat_prompt,
            llm=llm,
            memory=memory,
        ) | (lambda output: output["text"])

    if document_chat_chain_type == "Q&A Generation":
        return get_rag_qa_gen_chain(
            retriever,
            llm,
        )
    elif document_chat_chain_type == "Summarization":
        return get_rag_summarization_chain(
            summarization_prompt,
            retriever,
            llm,
        )
    else:
        return RetrievalQA.from_chain_type(
            llm=llm,
            chain_type=document_chat_chain_type,
            retriever=retriever,
            memory=memory,
            output_key="output_text",
        ) | (lambda output: output["output_text"])


def get_llm(
    provider: str,
    model: str,
    provider_api_key: str,
    temperature: float,
    max_tokens: int,
    azure_available: bool,
    azure_dict: dict[str, str],
):
    if azure_available and provider == "Azure OpenAI":
        return AzureChatOpenAI(
            openai_api_base=azure_dict["AZURE_OPENAI_BASE_URL"],
            openai_api_version=azure_dict["AZURE_OPENAI_API_VERSION"],
            deployment_name=azure_dict["AZURE_OPENAI_DEPLOYMENT_NAME"],
            openai_api_key=azure_dict["AZURE_OPENAI_API_KEY"],
            openai_api_type="azure",
            model_version=azure_dict["AZURE_OPENAI_MODEL_VERSION"],
            temperature=temperature,
            streaming=True,
            max_tokens=max_tokens,
        )

    elif provider_api_key:
        if provider == "OpenAI":
            return ChatOpenAI(
                model_name=model,
                openai_api_key=provider_api_key,
                temperature=temperature,
                streaming=True,
                max_tokens=max_tokens,
            )

        elif provider == "Anthropic":
            return ChatAnthropic(
                model=model,
                anthropic_api_key=provider_api_key,
                temperature=temperature,
                streaming=True,
                max_tokens_to_sample=max_tokens,
            )

        elif provider == "Anyscale Endpoints":
            return ChatAnyscale(
                model_name=model,
                anyscale_api_key=provider_api_key,
                temperature=temperature,
                streaming=True,
                max_tokens=max_tokens,
            )

    return None


def get_texts_and_retriever(
    uploaded_file_bytes: bytes,
    openai_api_key: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    k: int = DEFAULT_RETRIEVER_K,
    azure_kwargs: Optional[Dict[str, str]] = None,
    use_azure: bool = False,
) -> Tuple[List[Document], BaseRetriever]:
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
        embeddings_kwargs = {"openai_api_key": openai_api_key}
        if use_azure and azure_kwargs:
            embeddings_kwargs.update(azure_kwargs)
        embeddings = OpenAIEmbeddings(**embeddings_kwargs)

        bm25_retriever = BM25Retriever.from_documents(texts)
        bm25_retriever.k = k

        faiss_vectorstore = FAISS.from_documents(texts, embeddings)
        faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": k})

        ensemble_retriever = EnsembleRetriever(
            retrievers=[bm25_retriever, faiss_retriever],
            weights=[0.5, 0.5],
        )

        return texts, ensemble_retriever


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)
