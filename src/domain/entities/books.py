from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from src.domain.entities.users import UserDto


class BookRequestAddDto(BaseModel):
    user_id: int
    title: str = Field(min_length=5)
    description: str | None = Field(min_length=5, default=None)


class BookAddDto(BookRequestAddDto):
    created_at: datetime


class BookDto(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    url_text: str | None
    url_cover: str | None
    created_at: datetime


class BookWithAuthorDto(BookDto):
    author: Optional[UserDto]


class BookPatchRequestDto(BaseModel):
    user_id: int | None = None
    title: str | None = Field(min_length=5, default=None)
    description: str | None = Field(min_length=5, default=None)


class BookPatchDto(BookPatchRequestDto):
    id: int
