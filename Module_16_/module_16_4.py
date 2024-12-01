from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

# иммитация базы данных
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


# иммитация базы данных
"""
t1 = User(id=1, username="UrbanUser", age = 24)
users.append(t1)
t2 = User(id=2, username="UrbanTest", age = 36)
users.append(t2)
t3 = User(id=4, username="Admin", age = 42)
users.append(t3)
"""


@app.get("/")
async def main_page() -> str:
    return f'Главная страница'


@app.get("/users")
async def all_users() -> list[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", examples=['User'])],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=['24'])]
        ) -> User:
    if len(users) == 0:
        new_user_id = 1
    else:
        new_user_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=new_user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def upd_user(
        user_id: Annotated[int, Path(ge=1, le=50, description="Enter user_id", examples=['15'])],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", examples=['User'])],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=['24'])]
        ) -> User:
    try:
        user_ = list(filter(lambda i: i.id == user_id, users))
        find_user = users.index(user_[0])
        edit_users = users[find_user]
        edit_users.username = username
        edit_users.age = age
        return users[find_user]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def del_user(
        user_id: int = Path(ge=1, le=50, description="Enter user_id", examples=['15'])
        ) -> User:
    try:
        user_ = list(filter(lambda i: i.id == user_id, users))
        find_user = users.index(user_[0])
        delete_user = users.pop(find_user)
        return delete_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
