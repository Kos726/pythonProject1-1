from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page() -> str:
    return f'Главная страница'


@app.get("/user/admin")
async def admin_user() -> str:
    return f'Вы вошли как администратор'


@app.get("/user/{user_id}")
async def id_enter(user_id: int) -> str:
    return f'Вы вошли как пользователь №{user_id}'


@app.get("/user")
async def old_user(user_name: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {user_name}, Возраст: {age}'
