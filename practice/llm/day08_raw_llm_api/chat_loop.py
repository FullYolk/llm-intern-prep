from typing import List
import llm_client
from llm_client import MODEL_NAME
import openai
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

Messages = []
Messages.append({"role":"system", "content":"你是一个北航的学生助手"})

def get_llm_response(client,s):
    from llm_client import API_KEY
    if not API_KEY:
        logging.critical("APIKEY缺失！请检查.env文件！")
        return "配置错误 请联系管理员"
    try:
        logging.info("发送API请求...")
        Messages.append({"role":"user","content":s})       
        response = client.chat.completions.create(model=MODEL_NAME,messages=Messages,temperature=0.7)
        if response.choices[0].message.content != None:
            usage = response.usage
            logging.info(f"请求成功！Token消耗: Total={usage.total_tokens}, Prompt={usage.prompt_tokens}, Completion={usage.completion_tokens}")
            reply = response.choices[0].message.content
            Messages.append({"role":"assistant","content":reply})
            return response.choices[0].message.content
    except openai.RateLimitError:
        logging.warning("触发速率限制")
        return "我累了 请稍后重试"
    except Exception as e:
        logging.error(f"未知异常：{type(e).__name__} - {e}")
        return "发生了一点意外 请重试"

def chat_loop():
    client = llm_client.get_client()
    while True:
        s = input("请输入内容")
        if s == "exit" or s == "quit":
            break
        content = get_llm_response(client,s)
        print(content)
    

def main():
    chat_loop()
    
if __name__ == "__main__":
    main()