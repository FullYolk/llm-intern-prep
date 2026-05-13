from pydantic import BaseModel
from pydantic import ValidationError
from typing import Optional
from typing import List
from pydantic import Field
class StudentModel(BaseModel):
    name: str
    score: int

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default_session"
    user_id: Optional[int] = None

student = StudentModel(name="Alice", score=90)

class StrictStudent(BaseModel):

    name: str = Field(min_length=1, max_length=20, description="学生姓名")

    score: int = Field(ge=0, le=100, description="考试分数")

class ClassRoom(BaseModel):
    class_name: str
    students: List[StudentModel]

print("对象：", student)

print("转为字典:", student.model_dump())

s_str = StudentModel(name="Bob", score="85") 
print("自动把字符串'85'转为了整数:", repr(s_str.score)) 

req1 = ChatRequest(message="Hello llm")
print("\n带默认值的请求：",req1.model_dump())

data_from_frontend = {
    "class_name": "CS-01",
    "students": [
        {"name":"Alice", "score": 90},
        {"name":"Bob", "score": 85}
    ]
}

room = ClassRoom(**data_from_frontend)
print("\n班级对象:", room.class_name)
print("第一个学生名字:", room.students[0].name)


#bad_student = StrictStudent(name="", score=105)

# try:
#    s_error = StudentModel(name="Charlie", score="abc")
 #   print(s_error)
#except ValidationError as e:
#    print("\n被海关拦截了！报错信息：\n", e)