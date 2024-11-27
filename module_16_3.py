from fastapi import FastAPI, HTTPException

from pydantic import BaseModel, conint, constr

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


class User(BaseModel):
    username: constr(min_length=1, max_length=50)  # Имя пользователя от 1 до 50 символов
    age: conint(ge=0, le=120)  # Возраст от 0 до 120 лет


@app.get('/users')
async def get_users():
    return users


@app.post('/user/', response_model=str)
async def create_user(user: User):
    user_id = str(int(max(users, key=int)) + 1)
    user_info = f"Имя: {user.username}, возраст: {user.age}"
    users[user_id] = user_info
    return f"User {user_id} is registered"


@app.put('/user/{user_id}', response_model=str)
async def update_user(user_id: str, user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    users[user_id] = f"Имя: {user.username}, возраст: {user.age}"
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}', response_model=str)
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    users.pop(user_id)
    return f"The user {user_id} is deleted"
