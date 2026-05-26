from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
    model=os.getenv("LLM_MODEL"),
    temperature=0.0
)

prompt = ChatPromptTemplate([
    ("system","你是一个信息抽取助手，只需要输出JSON"),
    ("human","给定文本{text},按照以下格式输出{format_instructions}")
])

parser = JsonOutputParser()

chain = prompt | llm | parser

result = chain.invoke({
    "text":"张三是北航大二学生，他希望找Agent开发实习",
    "format_instructions": parser.get_format_instructions()
})

print(type(result))
print(result)
print(result["skills"])