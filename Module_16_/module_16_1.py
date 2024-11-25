from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
    return {"message": 'Главная страница'}


@app.get("/user/admin")
async def admin_user() -> dict:
    return {"message": 'Вы вошли как администратор'}


@app.get("/user/{user_id}")
async def id_enter(user_id: int) -> dict:
    return {"message": f'Вы вошли как пользователь №{user_id}'}


@app.get("/user")
async def old_user(user_name: str, age: int) -> dict:
    return {"message": f'Информация о пользователе. Имя: {user_name}, Возраст: {age}'}
