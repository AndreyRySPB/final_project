import logging

from sqlalchemy import NullPool, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.settings.settings import settings


engine = create_async_engine(settings.DB_URL)
engine_null_pool = create_async_engine(settings.DB_URL, poolclass=NullPool)

async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
async_session_maker_null_pool = async_sessionmaker(bind=engine_null_pool, expire_on_commit=False)


async def check_db():
    try:
        async  with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
        logging.info("База данных работает нормально.")
        return True
    except Exception as e:
        logging.info(f"Ошибка подключения к БД: {e}")
        return False