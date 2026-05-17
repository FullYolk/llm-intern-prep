from fastapi import FastAPI,HTTPException
from schemas import Todo,TodoCreate
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
import asyncio
import time
import os
import shutil
from fastapi import File,UploadFile
import uuid
app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_handler(request:Request, exc:ValueError):
    return JSONResponse(
        status_code=400,
        content={"error_type":"业务逻辑错误","message":str(exc)}
    )

fake_db:list[Todo] = []
current_id = 1

@app.middleware("http")
async def log_requests(request:Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    print(f"{request.method}, {request.url.path}, {end_time-start_time}")
    return response

@app.get("/todos",response_model = list[Todo])
def get_todos(completed:bool | None = None):
    if completed is None:
        return fake_db
    return [todo for todo in fake_db if todo.completed == completed]

@app.post("/todos",response_model = Todo, status_code = 201) #status_code?
def create_todo(todo:TodoCreate):
    global current_id
    new_todo = Todo(id=current_id, title=todo.title, completed=todo.completed)
    fake_db.append(new_todo)
    current_id += 1
    return new_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for i, todo in enumerate(fake_db):
        if todo.id == todo_id:
            fake_db.pop(i)
            return {"msg": "删除成功"}
    raise HTTPException(status_code=404,detail="未找到该TODO")

@app.get("/todos/{todo_id}")
def get_single_todo(todo_id:int,response_moedel = Todo):
    for todo in fake_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404,detail="没有找到这个Todo")

@app.get("/")
def read_root():
    return {"message": "hello,This is my first FastAPI backend"}

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/test-error")
def test_error():
    raise ValueError("测试：系统计算错误")

@app.post("/upload")
async def upload_file(file:UploadFile = File(...)):
    if file.content_type != "text/plain":
        raise HTTPException(status_code=400,detail="只能上传txt")
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    ext = os.path.splitext(file.filename)[1]
    safe_filename = f"{uuid.uuid4().hex}{ext}"
    
    file_path = os.path.join(upload_dir,safe_filename)

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    return {"filename" : file.filename, "size": file.size, "saved_path":file_path}

async def fake_video_streamer():
    words = ["Hello"," ","I"," ","am"," ","an"," "," AI"," ","Agent","!"]
    try:
        for word in words:
            yield f"data:{word}\n\n"
            await asyncio.sleep(0.5)
    except asyncio.CancelledError:
        print("警告 用户掐断了连接")
        raise
    finally:
        print("流式输出结束")

@app.get("/stream")
async def stream_text():
    return StreamingResponse(fake_video_streamer(), media_type="text/event-stream")
