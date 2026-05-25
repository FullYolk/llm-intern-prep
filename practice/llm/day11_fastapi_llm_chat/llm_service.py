import llm_client
from llm_client import MODEL_NAME
import logging

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
    recent_msgs = history[1:][-MAX_HISTORY_MESSAGE:]
    chat_histories[session_id] = [system_msg] + recent_msgs
#上下文需要限制长度

def stream_chat_with_history(session_id:str, user_message:str):
    if session_id not in chat_histories:
        chat_histories[session_id] = [{"role":"system","content":"你是一个得力的AI助手，针对Agent学习相关知识点做了特别优化"}]
    (chat_histories[session_id]).append({"role":"user","content":user_message})
    try:
        logging.info(f"开始呼叫 LLM (流式) | session_id: {session_id}")

        stream_response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=chat_histories[session_id],
        temperature=0.7,
        stream=True
        )
        full_reply = ""

        for chunk in stream_response:
            delta_content = chunk.choices[0].delta.content
            if delta_content:
                full_reply += delta_content
                yield f"data:{delta_content}\n\n"
    
        chat_histories[session_id].append({"role":"assistant","content":full_reply})
        trim_history(session_id)

        logging.info(f"[Stream Complete] 回复完成 | session_id: {session_id} | 回复字数: {len(full_reply)}")
    
        yield"data:[DONE]\n\n"       
    except Exception as e:
        logging.error(f"[Stream Failed] LLM 调用异常 | session_id: {session_id} | 错误: {str(e)}", exc_info=True)
        
        yield f"data: [ERROR] 大模型开小差了，请稍后再试\n\n"
        yield "data: [DONE]\n\n"