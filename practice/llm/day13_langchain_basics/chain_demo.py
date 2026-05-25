from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
    model=os.getenv("LLM_MODEL"),
    temperature=0.3
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个资深的程序员，你总是用{style}的语气回答问题。"),
    ("human", "请帮我解释一下什么是 {topic}？")
])

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({
    "style" : "极度暴躁但又很靠谱",
    "topic" : "LangChain"
})

print(result)