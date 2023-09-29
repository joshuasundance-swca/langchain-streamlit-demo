from functools import reduce
from typing import List

from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from langchain.prompts.chat import (
    ChatPromptTemplate,
)
from langchain.schema.language_model import BaseLanguageModel
from langchain.schema.runnable import RunnableSequence
from pydantic import BaseModel, field_validator, Field


class QuestionAnswerPair(BaseModel):
    question: str = Field(..., description="The question that will be answered.")
    answer: str = Field(..., description="The answer to the question that was asked.")

    @field_validator("question")
    def validate_question(cls, v: str) -> str:
        if not v.endswith("?"):
            raise ValueError("Question must end with a question mark.")
        return v


class QuestionAnswerPairList(BaseModel):
    QuestionAnswerPairs: List[QuestionAnswerPair]


PYDANTIC_PARSER: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=QuestionAnswerPairList,
)


templ1 = """You are a smart assistant designed to help college professors come up with reading comprehension questions.
Given a piece of text, you must come up with question and answer pairs that can be used to test a student's reading comprehension abilities.
Generate as many question/answer pairs as you can.
When coming up with the question/answer pairs, you must respond in the following format:
{format_instructions}

Do not provide additional commentary and do not wrap your response in Markdown formatting. Return RAW, VALID JSON.
"""
templ2 = """{prompt}
Please create question/answer pairs, in the specified JSON format, for the following text:
----------------
{input}"""
CHAT_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", templ1),
        ("human", templ2),
    ],
).partial(format_instructions=PYDANTIC_PARSER.get_format_instructions)


def combine_qa_pair_lists(
    qa_pair_lists: List[QuestionAnswerPairList],
) -> QuestionAnswerPairList:
    def reducer(
        accumulator: QuestionAnswerPairList,
        current: QuestionAnswerPairList,
    ) -> QuestionAnswerPairList:
        return QuestionAnswerPairList(
            QuestionAnswerPairs=accumulator.QuestionAnswerPairs
            + current.QuestionAnswerPairs,
        )

    return reduce(
        reducer,
        qa_pair_lists,
        QuestionAnswerPairList(QuestionAnswerPairs=[]),
    )


def get_qa_gen_chain(llm: BaseLanguageModel) -> RunnableSequence:
    return (
        CHAT_PROMPT | llm | OutputFixingParser.from_llm(llm=llm, parser=PYDANTIC_PARSER)
    )