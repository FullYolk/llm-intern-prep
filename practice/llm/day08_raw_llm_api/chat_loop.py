import llm_client
from llm_client import MODEL_NAME
import openai
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

messages = [{"role":"system", "content":"你是一个北航的学生助手"}]

def get_llm_response(client,s):
    if not llm_client.API_KEY:
        logging.critical("APIKEY缺失！请检查.env文件！")
        return "配置错误 请联系管理员"
    try:
        logging.info("发送API请求...")
        messages.append({"role":"user","content":s})       
        response = client.chat.completions.create(model=MODEL_NAME,messages=messages,temperature=0.7)
        if not response.choices:
            logging.error("模型返回 choices 为空")
            return "模型没有返回内容"
        reply = response.choices[0].message.content
        if not reply:
            logging.warning("模型返回空内容")
            return "模型返回了空结果"
        else:
            usage = response.usage
            logging.info(f"请求成功！Token消耗: Total={usage.total_tokens}, Prompt={usage.prompt_tokens}, Completion={usage.completion_tokens}")
            reply = response.choices[0].message.content
            messages.append({"role":"assistant","content":reply})
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
        s = input("请输入内容:")
        if s == "exit" or s == "quit":
            break
        content = get_llm_response(client,s)
        print(content)
    

def main():
    chat_loop()
    
if __name__ == "__main__":
    main()