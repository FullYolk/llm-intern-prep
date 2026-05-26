from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
    model=os.getenv("LLM_MODEL"),
    temperature=0.0
)

prompt = ChatPromptTemplate.from_messages([
    ("system","你是一个资深的HR助手，请用一句简短的话总结候选人的核心亮点。"),
    ("human","候选人信息{text}")
])

parser = StrOutputParser()

chain = prompt | llm | parser

inputs = [
    {"text": "张三想找后端实习，他会Java。"},
    {"text": "李四喜欢AI，想找Agent实习，熟悉Python。"},
    {"text": "王五是产品经理，不懂代码。"}
]

result = chain.batch(inputs,config={"max_concurrency":3})

print(type(result))
print(result)

for chunk in chain.stream({"text":"请给我写一篇关于LangChain的100字介绍"}):
    print(chunk, end="", flush=True)