import llm_client
from llm_client import MODEL_NAME

client = llm_client.get_client()

chat_histories = {} #实际工程中接Redis等数据库

MAX_HISTORY_MESSAGE = 10

def chat_with_history(session_id: str, user_message:str) -> str:
    if session_id not in chat_histories:
        chat_histories[session_id] = [{"role":"system","content":"你是一个得力的AI助手，针对Agent学习相关知识点做了特别优化"}]
    (chat_histories[session_id]).append({"role":"user","content":user_message})
    response = client.chat.completions.create(model=MODEL_NAME,messages=chat_histories[session_id],temperature=0.7)
    reply_message = response.choices[0].message
    reply_text = reply_message.content
    if not reply_text:
        raise ValueError("模型返回空内容")
    (chat_histories[session_id]).append({"role":"assistant","content":reply_text})
    trim_history(session_id)
    return reply_text

def clear_session_history(session_id:str) -> bool:
    if session_id in chat_histories:
        chat_histories.pop(session_id)
        return True
    return False

def trim_history(session_id: str):
    history = chat_histories[session_id]
    if len(history) <= MAX_HISTORY_MESSAGE + 1:
        return
    
    system_msg = history[0]
    recent_msgs = history[1:][-MAX_HISTORY_MESSAGE]
    chat_histories[session_id] = [system_msg] + recent_msgs
#上下文需要限制长度