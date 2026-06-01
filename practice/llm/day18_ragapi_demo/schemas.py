from pydantic import BaseModel, Field
from typing import List

class SourceItem(BaseModel):
    filename:str = Field(description="知识来源文件名")
    score:float = Field(description="向量检索的距离得分")
    preview:str = Field(description="来源文档的文本预览")

class AskRequest(BaseModel):
    query:str = Field(min_length=1, max_length=2000,description="向大模型提出的问题")
    k:int = Field(default=3, ge=1, le=10, description="召回的topk")

class AskResponse(BaseModel):
    answer:str = Field(description="模型基于知识库生成的回答")
    sources:List[SourceItem] = Field(description="引用来源明细")


