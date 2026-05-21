from pydantic import BaseModel,Field

class ChatRequest(BaseModel):
    #前端发的数据
    session_id:str = Field(default="default", description="会话id")
    message:str = Field(min_length=1, max_length=5000, description="用户提问内容")

class ChatResponse(BaseModel):
    #我们返回的
    session_id:str
    reply:str