from fastapi import Form, Path, HTTPException
from fastapi import APIRouter
from homework6 import db
from db import *
from models import InputUser, User

router = APIRouter()


@router.post("/add_user", description="Добавить Пользователя")
async def add_user(name: str = Form(...), last_name: str = Form(...), email: str = Form(...),
                   password: str = Form(...)):
    query = users_db.insert().values(
        name=name,
        last_name=last_name,
        email=email,
        password=password
    )
    await db.execute(query)
    return {"message": "User added"}


@router.post("/user/{user_id}", description="Просмотреть  Пользователя")
async def viev_user(user_id: int, user: User):
    query = users_db.select().where(users_db.c.id == user_id)
    user_quer = await db.fetch_one(query)
    if not user_quer:
        raise HTTPException(status_code=404, detail="User not found or has no orders")
    return user_quer




@router.put("/update_user/{user_id}", description="Изменить пользователя")
async def update_user(user_id: int, user: InputUser):
    query = users_db.update().where(users_db.c.id == user_id).values(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        password=user.password
    )
    await db.execute(query)
    return {"message": "User updated"}


@router.get("/all_users/", response_model=list[User], description="Просмотреть всех пользователей")
async def read_users():
    query = users_db.select()
    return await db.fetch_all(query)


@router.delete("/del_users/{user_id}", description="Удалить пользователя")
async def delete_user(user_id: int):
    query = users_db.delete().where(users_db.c.id == user_id)
    await db.execute(query)
    return {'message': 'User deleted'}


@router.get("/user_orders/{user_id}")
async def get_user_orders(user_id: int = Path(..., title="User ID")):
    query = orders_db.select().where(orders_db.c.user_id == user_id)
    user_orders = await db.fetch_all(query)
    if not user_orders:
        raise HTTPException(status_code=404, detail="User not found or has no orders")
    return user_orders
