from fastapi import FastAPI

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_message():
    return users


@app.post('/user/{username}/{age}')
async def create_message(username: str, age: int):
    user_id = str(int(max(users, key=int)) + 1)
    user_info = f"Имя: {username}, возраст: {age}"
    users[user_id] = user_info
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_message(user_id: int, username: str, age: int):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_message(user_id):
    users.pop(user_id)
