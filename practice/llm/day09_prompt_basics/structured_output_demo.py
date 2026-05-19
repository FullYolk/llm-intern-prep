import llm_client
from llm_client import MODEL_NAME
from pydantic import BaseModel
from typing import List
import json
from pydantic import ValidationError

class StudentProfile(BaseModel):
    name:str
    school:str
    grade:str
    target_role:str
    skills:List[str]

def extract_profile(text:str):
    messages = []
    messages.append({"role":"system", "content":"你的任务是从用户输入的文本中提取信息，核心要求是必须且只能输出合法的JSON字符串，JSON的字段必须按顺序严格对应：name, school, grade, target_role, skills。不要包裹任何markdown语法，不要有任何多余输出与解释，我将使用json.loads对其进行提取，因此务必不要输出任何额外内容，仅输出合法JSON字符串"})
    messages.append({"role":"user","content":text})
    client = llm_client.get_client()
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages,temperature=0.0)
    content = response.choices[0].message.content
    try:
        dic = json.loads(content)
        zhangsan = StudentProfile(**dic)
        print(f"提取成功！姓名：{zhangsan.name} 学校：{zhangsan.school} 年级：{zhangsan.grade} 目标：{zhangsan.target_role} 技能:{zhangsan.skills}" )
    except json.JSONDecodeError:
        print("大模型没成功说出JSON！")
    except ValidationError:
        print("漏掉了某些字段！")

def main():
    te = input("请输入文本：")
    extract_profile(te)

if __name__ == "__main__":
    main()    