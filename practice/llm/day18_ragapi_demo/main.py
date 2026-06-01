from fastapi import FastAPI,HTTPException
from schemas import AskRequest,AskResponse
from rag_service import answer_with_rag
import logging

app = FastAPI(title="RAG微服务")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

@app.get("/health")
def check_health():
    return {"status":"ok"}

@app.post("/ask",response_model=AskResponse)
def ask(request:AskRequest):
    try:
        safe_query = request.query.replace("\n", " ")
        if len(safe_query) > 30:
            safe_query = safe_query[:30] + "..."
        logging.info(f"收到请求|query:{safe_query}|k:{request.k}")
        return AskResponse(**answer_with_rag(request.query, request.k))
    except Exception as e:
        logging.error(f"发生错误，异常为{str(e)}",exc_info=True)
        raise HTTPException(status_code=500,detail="llm service error")