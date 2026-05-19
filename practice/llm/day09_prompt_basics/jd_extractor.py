from pydantic import BaseModel, ValidationError
import llm_client
from llm_client import MODEL_NAME
from typing import List
import json

class JDExtraction(BaseModel):
    job_title:str
    tech_stack:List[str]
    requires_java:bool
    requires_rag_agent:bool
    duration_requirement:str

def jd_exrtactor(text:str):
    schema_str = JDExtraction.model_json_schema()
    messages = []
    messages.append({"role":"system", "content":f"你是一个资深的HR助手，擅长从招聘JD中提取结构化信息。核心要求是必须且只能输出合法的JSON字符串，JSON的字段要求为：{schema_str}不要包裹任何markdown语法，不要有任何多余输出与解释，我将使用json.loads对其进行提取，因此务必不要输出任何额外内容，仅输出合法JSON字符串"})
    messages.append({"role": "user", "content": "提取这段JD：【急招】后端开发实习生（Java方向）。要求：熟悉Java基础，了解Spring Boot框架，掌握MySQL和Redis。了解微服务架构优先。要求每周到岗5天，实习至少6个月。"})
    messages.append({"role": "assistant", "content": '{"job_title":"后端开发实习生","tech_stack":["Java","Spring Boot","MySQL","Redis","微服务"],"requires_java":true,"requires_rag_agent":false,"duration_requirement":"至少6个月"}'})
    messages.append({"role":"user","content":text})
    client = llm_client.get_client()
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages,temperature=0.0)
    content = response.choices[0].message.content
    try:
        dic = json.loads(content)
        info = JDExtraction(**dic)
        print("✅ 提取成功！")
        print(f"岗位名称: {info.job_title}")
        print(f"技术栈: {info.tech_stack}")
        print(f"要求Java: {info.requires_java}")
        print(f"要求RAG/Agent: {info.requires_rag_agent}")
        print(f"实习时间: {info.duration_requirement}")
    except json.JSONDecodeError:
        print("大模型没成功说出JSON！")
    except ValidationError:
        print("漏掉了某些字段！")

def main():
    target_jd = """
    【大模型AI后端实习生】团队主要负责通用Agent平台建设。要求：
    1. 计算机相关专业，Python基础扎实；
    2. 熟练使用FastAPI或Flask，了解Docker；
    3. 对大语言模型有强烈热情，了解Prompt调优，有过LangChain、LangGraph或RAG相关项目经验者优先；
    4. 实习期保证4个月以上，每周4天。
    5. 会Go或Java是加分项，但非必需。
    """
    jd_exrtactor(target_jd)

if __name__ == "__main__":
    main()
