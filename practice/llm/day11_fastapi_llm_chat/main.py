from fastapi import FastAPI,HTTPException
from schemas import ChatRequest,ChatResponse
from llm_service import chat_with_history, clear_session_history

app = FastAPI(title="Agent学习助手API")

@app.post("/chat",response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    try:
        session_id = request.session_id
        message = request.message
        reply = chat_with_history(session_id, message)
        return ChatResponse(session_id=session_id,reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@app.get("/health")
def health_check():
    return {"status":"ok","message":"service is running"}

@app.delete("/sessions/{session_id}")
def clear_session(session_id:str):
    succsess = clear_session_history(session_id)
    if succsess:
        return {"status":"success","message":f"会话{session_id}已清空"}
    else:
        raise HTTPException(status_code=404,detail="未找到该会话")