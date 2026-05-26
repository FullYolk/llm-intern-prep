from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os

load_dotenv()

class CandidateProfile(BaseModel):
    name:str = Field(default=None,description="候选人姓名")
    school:str = Field(default=None,description="学校")
    skills:list[str] = Field(default=None,description="技能列表")
    target_role:str = Field(default=None,description="目标岗位")

llm = ChatOpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
    model=os.getenv("LLM_MODEL"),
    temperature=0.0
)

prompt = ChatPromptTemplate.from_messages([
    ("system","你是一个极其严谨的信息抽取助手，只需要输出JSON,规则：绝不能基于常识进行推断，原文中没有提到的字段必须输出 null。"),
    ("human","给定文本{text},按照以下格式输出{format_instructions}")
])

parser = PydanticOutputParser(pydantic_object=CandidateProfile)

chain = prompt | llm | parser

result = chain.invoke({
    "text":"玩机器是达尔豪斯大学学生，他擅长解说",
    "format_instructions": parser.get_format_instructions()
})

print(type(result))
print(result.name)
print(result.skills)
print(result.target_role)