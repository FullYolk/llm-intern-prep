import llm_client
from llm_client import MODEL_NAME

def chat_once(s:str) -> str:
    messages = []
    messages.append({"role":"system", "content":"你是一个北航的学生助手"})
    messages.append({"role":"user","content":s})
    client = llm_client.get_client()
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages,temperature=0.7)
    content = response.choices[0].message.content
    return content

def main():
    user_query = input("请输入内容:")
    print(chat_once(user_query))
    
if __name__ == "__main__":
    main()