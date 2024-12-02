from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()

# иммитация базы данных
users = []

# настраиваем папку с шаблонами
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int = None
    username: str
    age: int


"""
# иммитация базы данных
t1 = User(id=1, username="UrbanUser", age=24)
users.append(t1)
t2 = User(id=2, username="UrbanTest", age=36)
users.append(t2)
t3 = User(id=3, username="Copybara", age=60)
users.append(t3)
"""


@app.get("/")
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        find_user = list(filter(lambda i: i.id == user_id, users))
        index_user = users.index(find_user[0])
        return templates.TemplateResponse("users.html", {"request": request, "user": users[index_user]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User ID was not found")


@app.post("/user/{username}/{age}")
async def post_user(
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
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=50, description="Enter user_id", examples=['15'])],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", examples=['User'])],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=['24'])]
        ) -> User:
    try:
        find_user = list(filter(lambda i: i.id == user_id, users))
        index_user = users.index(find_user[0])
        edit_users = users[index_user]
        edit_users.username = username
        edit_users.age = age
        return users[index_user]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: int = Path(ge=1, le=50, description="Enter user_id", examples=['15'])
        ) -> User:
    try:
        find_user = list(filter(lambda i: i.id == user_id, users))
        index_user = users.index(find_user[0])
        del_user = users.pop(index_user)
        return del_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
