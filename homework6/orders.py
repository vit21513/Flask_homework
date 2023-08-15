from fastapi import Form, APIRouter
from starlette.templating import Jinja2Templates
from homework6 import db
from db import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()
from models import InputOrder, Order


@router.post("/add_order")
async def add_order(user_id: int = Form(...), goods_id: int = Form(...), order_status: str = Form(...)):
    query = orders_db.insert().values(
        user_id=user_id,
        goods_id=goods_id,
        order_status=order_status
    )
    await db.execute(query)
    return {"message": "Order added"}


@router.put("/update_order/{order_id}")
async def update_order(order_id: int, order: InputOrder):
    query = orders_db.update().where(orders_db.c.id == order_id).values(
        user_id=order.user_id,
        goods_id=order.goods_id,
        order_status=order.order_status
    )
    await db.execute(query)
    return {"message": "Order updated"}


@router.get("/all_orders/", response_model=list[Order], description="Просмотреть все заказы")
async def read_orders():
    query = orders_db.select()
    return await db.fetch_all(query)


@router.delete("/del_orders/{orders_id}", description="Удалить заказ")
async def delete_orders(orders_id: int):
    query = orders_db.delete().where(orders_db.c.id == orders_id)
    await db.execute(query)
    return {'message': 'Orders deleted'}


