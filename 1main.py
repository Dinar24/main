from fastapi import FastAPI

app = FastAPI()


@app.get('/user/admin')
async def call_admin():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def call_id(user_id: int):
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def call_user(username: str, age: int):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get('/')
async def call():
    return {'message': 'Главная страница'}

# uvicorn main2:app --reload