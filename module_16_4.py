from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_message():
    return users


# get запрос по маршруту '/users' теперь возвращает список users.

@app.post('/user/{username}/{age}')
async def create_message(username: str, age: int):
    id = 0
    if len(users) > 0:
        id = len(users)
    else:
        id = 1
    print(id)
    new_user = User(id=id, username=username, age=age)
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
async def delete_message(user_id):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
