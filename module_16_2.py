from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def welcome():
    return {'message': 'Вы вошли как Администратор'}


@app.get('/user/{username}/{age}')
async def welcome(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                  age: Annotated[int, Path(ge=5, le=120, description='Enter age')]):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get('/user/{user_id}')
async def welcome(user_id: Annotated[int, Path(
    title="User ID",
    description="Enter User ID",
    ge=1,
    le=100
)]):
    return {'message': f'Вы вошли как пользователь № {user_id}'}
