from fastapi import FastAPI,HTTPException
from schemas import ChatRequest,ChatResponse
from llm_service import chat_with_history, clear_session_history
import logging

app = FastAPI(title="Agent学习助手API")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

@app.post("/chat",response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    try:
        session_id = request.session_id
        message = request.message

        logging.info(f"收到聊天请求 | session_id{session_id}")

        reply = chat_with_history(session_id, message)
        return ChatResponse(session_id=session_id,reply=reply)
    except Exception as e:
        logging.error(f"处理 session_id = {session_id} 时发生异常: {str(e)}",exc_info=True)
        raise HTTPException(status_code=500,detail="LLM service failed")
#真实项目不要直接暴露异常
@app.get("/health")
def health_check():
    return {"status":"ok","message":"service is running"}

@app.delete("/sessions/{session_id}")
def clear_session(session_id:str):
    success = clear_session_history(session_id)
    if success:
        return {"status":"success","message":f"会话{session_id}已清空"}
    else:
        raise HTTPException(status_code=404,detail="未找到该会话")