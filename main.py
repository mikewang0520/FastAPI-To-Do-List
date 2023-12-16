"""
Advantages of FastAPI:
1. It's just plain Python
2. Asynchronous build-in support
3. Automatic data validation with Pydantic
4. Can declare Python types
5. Errors are in JSON format
6. Authentication build-in support
7. Automatic documentation with Swagger UI and Redoc
"""

from typing import Union
from fastapi import FastAPI
from models import Todo

app = FastAPI()

todos = []

# Get all todos
@app.get("/todos")   # Path decorator
async def get_todos():
    return {"todos": todos}

# Get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "Todo not found."}

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added."}

# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "Todo not found."}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been deleted."}
    return {"message": "Todo not found."}

