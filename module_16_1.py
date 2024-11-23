from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def welcome():
    return {'message': 'Вы вошли как Администратор'}


@app.get('/user/{user_id}')
async def welcome(user_id):
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user/{username}/{age}')
async def welcome(username, age):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


