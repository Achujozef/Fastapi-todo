from fastapi import FastAPI
from models import Todo
app = FastAPI()

todos=[]
#get all todo
@app.get("/todos")
async def get_todos():
    return {"Todos are ":todos}
#create a todo
@app.post("/todos")
async def post_todos(new_todo:Todo):
    todos.append(new_todo)
    return {"new Todos are ":todos}

#get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id:int):
    return next((todo for todo in todos if todo.id ==todo_id),"No todos Found") 

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int):
    todo= next((todo for todo in todos if todo.id == todo_id), "todo nOt FOund")
    todos.remove(todo)
    return todos

@app.put("/todos/{todo_id}")
async def delete_todo(todo_id:int, todo_obj:Todo):
    todo= next((todo for todo in todos if todo.id==todo_id),"Todo Not FOund")
    todo.item =todo_obj.item
    return {"Todo Changed":todo}