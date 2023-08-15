from fastapi import Form, APIRouter, Path, HTTPException
from starlette.templating import Jinja2Templates
from homework6 import db
from models import InputGoods, Goods
from db import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.post("/add_goods")
async def add_goods(name_goods: str = Form(...), description: str = Form(...), price: float = Form(...,gt=0, le=10000)):
    query = goods_db.insert().values(
        name_goods=name_goods,
        description=description,
        price=price
    )
    await db.execute(query)
    return {"message": "Goods added"}


@router.put("/update_goods/{goods_id}")
async def update_goods(goods_id: int, goods: InputGoods):
    query = goods_db.update().where(goods_db.c.id == goods_id).values(
        name_goods=goods.name_goods,
        description=goods.description,
        price=goods.price
    )
    await db.execute(query)
    return {"message": "Goods updated"}


@router.get("/all_goods/", response_model=list[Goods], description="Просмотреть все товары")
async def read_goods():
    query = goods_db.select()
    return await db.fetch_all(query)


@router.delete("/del_goods/{goods_id}", description="Удалить товар")
async def delete_goods(goods_id: int):
    query = goods_db.delete().where(goods_db.c.id == goods_id)
    await db.execute(query)
    return {'message': 'Goods deleted'}


@router.get("/goods_orders/{goods_id}")
async def get_user_goods(goods_id: int = Path(..., title="Goods ID")):
    query = orders_db.select().where(orders_db.c.goods_id == goods_id)
    goods_orders = await db.fetch_all(query)
    if not goods_orders:
        raise HTTPException(status_code=404, detail="orders this goods not found")
    return goods_orders


