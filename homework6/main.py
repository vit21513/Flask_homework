import uvicorn
from db import *
from fastapi import FastAPI, Request, HTTPException
import users
import orders
import goods

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(users.router, tags=['Пользователи'])
app.include_router(goods.router, tags=['Товар'])
app.include_router(orders.router, tags=['Заказы'])

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        # host="127.0.0.1",
        # port=8000,
        reload=True
    )
