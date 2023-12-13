from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnablePassthrough

from research_assistant.search.web import get_search_chain
from research_assistant.writer import get_writer_chain
from langchain.llms.base import BaseLLM
from langchain.schema.runnable import Runnable


def get_chain(search_llm: BaseLLM, writer_llm: BaseLLM) -> Runnable:
    chain_notypes = RunnablePassthrough().assign(
        research_summary=get_search_chain(search_llm),
    ) | get_writer_chain(writer_llm)

    class InputType(BaseModel):
        question: str

    return chain_notypes.with_types(input_type=InputType)
