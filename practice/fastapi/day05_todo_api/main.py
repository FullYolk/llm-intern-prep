from fastapi import FastAPI,HTTPException
from schemas import Todo,TodoCreate
app = FastAPI()

fake_db:list[Todo] = []
current_id = 1

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
    for todo in fake_db:
        if todo.id == todo_id:
            fake_db.pop(todo)
            return {"msg": "删除成功"}
    raise HTTPException(status_code=404,detail="未找到该TODO")

@app.get("/todos/{todo_id}")
def get_single_todo(todo_id:int):
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
