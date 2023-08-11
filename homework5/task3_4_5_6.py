# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Создайте HTML шаблон для отображения списка пользователей.

from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class New_user(BaseModel):
    name: str
    email: str
    password: str


list_user = [User(id=1, name="Ivan", email="test@test.ru", password="qwerty"),
             User(id=2, name="Maria", email="mashat@test.ru", password="12345"),
             ]


@app.get("/", response_model=list[User], summary='просмотреть всех пользователей', tags=['Пользователи'])
async def read_tasks():
    return list_user


@app.post("/new_user/", response_model=User, summary='добавить  пользователя')
async def create_user(user: New_user):
    id = len(list_user) + 1
    newUser = User
    newUser.id = id
    newUser.name = user.name
    newUser.email = user.email
    newUser.password = user.password
    list_user.append(newUser)
    return newUser


@app.put("/user_edit/{id}", response_model=User, summary='изменить  пользователя')
async def put_user_edit(id: int, edit_user: New_user):
    for user in list_user:
        if user.id == id:
            user.name = edit_user.name
            user.email = edit_user.email
            user.password = edit_user.password
            return user
    raise HTTPException(status_code=404, detail="user not found")


@app.delete("/user_del/{id}", summary='удалить пользователя')
async def delete_task(id: int):
    for user in list_user:
        if user.id == id:
            list_user.remove(user)
            return list_user
    raise HTTPException(status_code=404, detail="user not found")


@app.get("/all_user/", response_class=HTMLResponse)
async def read_all(request: Request):
    all = []
    for user in list_user:
        all.append(f'id={user.id},name={user.name},email={user.email}')

    return templates.TemplateResponse("index.html", {"request": request, "all": all})


if __name__ == '__main__':
    uvicorn.run(
        "task3:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
