from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class User(BaseModel):
    
    name: str
    email: str
    age: int
    student_id: str
    department: str
    year: int
    gpa: float
    courses: List[str]

users: Dict[int, User] = {}

@app.post("/users/{id}")
def create_user(id: int, user: User):
    if id in users:
        raise HTTPException(status_code=400, detail="User ID already exists!")
    users[id] = user
    return user

@app.get("/users", response_model=List[User])
def get_all_users():
    return list(users.values())

@app.get("/users/{id}", response_model=User)
def get_user_by_id(id: int):
    if id in users:
        return users[id]
    raise HTTPException(status_code=404, detail="User not found!")

@app.put("/users/{id}")
def update_user(id: int, updated_user: User):
    if id in users:
        users[id] = updated_user
        return updated_user
    raise HTTPException(status_code=404, detail="User not found!!")

@app.delete("/users/{id}")
def delete_user(id: int):
    if id in users:
        del users[id]
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
