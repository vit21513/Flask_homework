from datetime import datetime

import databases
import sqlalchemy
import sqlalchemy as sqlalchemy

from settings import settings

db = databases.Database(settings.DATABASE_URL)
mdt = sqlalchemy.MetaData()
users_db = sqlalchemy.Table("users", mdt,
                            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("name", sqlalchemy.String(32)),
                            sqlalchemy.Column("last_name", sqlalchemy.String(32)),
                            sqlalchemy.Column("email", sqlalchemy.String(128)),
                            sqlalchemy.Column("password", sqlalchemy.String(64)),

                            )

goods_db = sqlalchemy.Table("goods", mdt,
                            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("name_goods", sqlalchemy.String(128)),
                            sqlalchemy.Column("description", sqlalchemy.String(500)),
                            sqlalchemy.Column("price", sqlalchemy.FLOAT(128)),
                            )

orders_db = sqlalchemy.Table("orders", mdt,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'),
                                               nullable=False),
                             sqlalchemy.Column("goods_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('goods.id'),
                                               nullable=False),
                             sqlalchemy.Column("data", sqlalchemy.DateTime(), default=datetime.now),
                             sqlalchemy.Column("order_status",
                                               sqlalchemy.String(50)), )

engine = sqlalchemy.create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False})
mdt.create_all(engine)
