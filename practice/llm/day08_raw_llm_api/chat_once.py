from typing import List
import llm_client
from llm_client import MODEL_NAME

def chat_once(s:str) -> str:
    Message = []
    Message.append({"role":"system", "content":"你是一个北航的学生助手"})
    Message.append({"role":"user","content":s})
    client = llm_client.get_client()
    response = client.chat.completions.create(model=MODEL_NAME,messages=Message,temperature=0.7)
    print(response.choices[0].message.content)

def main():
    user_query = input("请输入内容:")
    chat_once(user_query)
    
if __name__ == "__main__":
    main()