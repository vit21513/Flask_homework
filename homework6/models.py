from pydantic import BaseModel, Field


class InputUser(BaseModel):
    name: str = Field(title="name", min_length=2)
    last_name: str = Field(title="last_name", min_length=2)
    email: str = Field(title="E-mail", min_length=5)
    password: str = Field(title="password", min_length=5)


class User(InputUser):
    id: int


class InputGoods(BaseModel):
    name_goods: str = Field(title="name_goods", min_length=2)
    description: str = Field(title="description", min_length=2)
    price: float = Field(title="price", gt=0, le=10000)


class Goods(InputGoods):
    id: int


class InputOrder(BaseModel):
    user_id: int
    goods_id: int


class Order(InputOrder):
    id: int
