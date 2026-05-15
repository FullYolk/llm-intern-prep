from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
    title: str = Field(min_length=1,max_length=100)
    completed: bool = False

class Todo(TodoCreate):
    id:int