from typing import Annotated

from fastapi import Query, Depends
from pydantic import BaseModel


class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(default=1, ge=1, description="Номер страницы")]
    per_page: Annotated[
        int | None,
        Query(default=3, ge=1, lt=30, description="Количество на странице"),
    ]


PaginationDep = Annotated[PaginationParams, Depends()]