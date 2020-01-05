# -*- coding: utf-8 -*-

import databases
from loguru import logger
import sqlalchemy

# from sqlalchemy import JSON
# from sqlalchemy import Boolean
# from sqlalchemy import Column
# from sqlalchemy import DateTime
# from sqlalchemy import Integer
# from sqlalchemy import MetaData
# from sqlalchemy import String
# from sqlalchemy import Table
# from sqlalchemy import create_engine
# from sqlalchemy.pool import QueuePool

from settings import SQLALCHEMY_DATABASE_URI

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URI,
    poolclass=sqlalchemy.pool.QueuePool,
    max_overflow=10,
    pool_size=100,
)
metadata = sqlalchemy.MetaData()
database = databases.Database(SQLALCHEMY_DATABASE_URI)


def create_db():
    metadata.create_all(engine)
    logger.info(f"Creating tables")


async def connect_db():
    await database.connect()
    logger.info(f"connecting to database")


async def disconnect_db():
    await database.disconnect()
    logger.info(f"disconnecting from database")


# users = Table(
#     "users",
#     metadata,
#     Column("user_id", String(length=100), primary_key=True),
#     Column("user_name", String(length=50), unique=True, nullable=False),
#     Column("first_name", String(length=150)),
#     Column("last_name", String(length=150)),
#     Column("email", String(length=200), unique=True, nullable=False),
#     Column("website", String(length=150)),
#     Column("password", String(length=50)),
#     Column("description", String(length=2000)),
#     Column("date_created", DateTime()),
#     Column("date_updated", DateTime()),
#     Column("is_active", Boolean(), default=True),
#     Column("is_superuser", Boolean(), default=True),
# )
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("pk", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, index=True),
    sqlalchemy.Column("last_login", sqlalchemy.DateTime, index=True),
    sqlalchemy.Column("github_id", sqlalchemy.Integer, index=True),
    sqlalchemy.Column("username", sqlalchemy.String, index=True),
    sqlalchemy.Column("is_admin", sqlalchemy.Boolean, index=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("avatar_url", sqlalchemy.String),
)
