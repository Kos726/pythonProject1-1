from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# иммитация базы данных
users = {'1': 'Имя: Exemple, Возраст: 18'}


@app.get("/")
async def main_page() -> str:
    return f'Главная страница'


@app.get("/users")
async def all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", examples=['User'])],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=['24'])]
        ) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f'User {user_id} is registred'


@app.put("/user/{user_id}/{username}/{age}")
async def upd_user(
        user_id: Annotated[int, Path(ge=1, le=50, description="Enter user_id", examples=['15'])],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", examples=['User'])],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=['24'])]
        ) -> str:
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete("/user/{user_id}")
async def del_user(
        user_id: int = Path(ge=1, le=50, description="Enter user_id", examples=['15'])
        ) -> str:
    del_user_ = users.pop(str(user_id))
    return f'The user {user_id} has been deleted ({del_user_})'
