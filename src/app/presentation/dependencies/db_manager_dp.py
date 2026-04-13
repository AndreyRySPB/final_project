from typing import Annotated

from fastapi import Depends

from src.infrastructure.connectors.db_conn import async_session_maker
from src.infrastructure.managers.db_manager import DBManager


async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db

DBManagerDep = Annotated[DBManager, Depends(get_db)]
