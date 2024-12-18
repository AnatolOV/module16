from fastapi import FastAPI, HTTPException, status, Body, Request
from pydantic import BaseModel, conint
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List

templates = Jinja2Templates(directory='templates')

app = FastAPI()
users = []

class User(BaseModel):
    id: int = None
    username: str
    age: conint(ge=0)


@app.get('/')
async def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html',{'request': request, 'users': users})


@app.get('/user/{user_id}')
async def get_message(request: Request, user_id: int):
    print(users[user_id -1].age)
    user = users[user_id-1]
    return templates.TemplateResponse('users.html',{
        "request": request,
        "user": user
    })


@app.post('/user/{username}/{age}')
async def create_message(username: str, age: int):
    user_id = (max([user.id for user in users], default=0) + 1)
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_message(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
        else:
            raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_message(user_id: str):
    for index, user in enumerate(users):
        if str(user.id) == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
