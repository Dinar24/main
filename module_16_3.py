from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                 description='Enter username',
                                                 example='UrbanUser')],
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             description='Enter age',
                                             example='24')]):
    new_index = str(int(max(users, key=int)) + 1)
    users[new_index] = f"Имя: {username}, возраст: {age}"
    return f"User {new_index} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id: Annotated[int, Path(ge=0,
                                             le=100,
                                             description='Enter id',
                                             example='1')],
                   username: Annotated[str, Path(min_length=5,
                                                 max_length=20,
                                                 description='Enter username',
                                                 example='UrbanUser')],
                   age: Annotated[int, Path(ge=18,
                                            le=120,
                                            description='Enter age',
                                            example='24')]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=0,
                                             le=100,
                                             description='Enter id',
                                             example='1')]):
    users.pop(str(user_id))
    return f"User {user_id} is deleted"


@app.get('/user')
async def get_user():
    return users
