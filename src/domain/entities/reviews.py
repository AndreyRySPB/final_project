from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from src.domain.entities.books import BookDto
from src.domain.entities.users import UserDto


class ReviewsRequestAddDto(BaseModel):
    book_id: int
    text: str = Field(min_length=5)
    rating: int = Field(ge=0, le=5, default=0)


class ReviewsAddDto(ReviewsRequestAddDto):
    user_id: int
    created_at: datetime


class ReviewDto(BaseModel):
    id: int
    book_id: int
    user_id: int
    text: str
    rating: int
    created_at: datetime


class ReviewWithBookAndUserDto(ReviewDto):
    user: Optional[UserDto]
    book: Optional[BookDto]


class ReviewPatchRequestDto(BaseModel):
    book_id: int | None = None
    user_id: int | None = None
    text: str | None = Field(min_length=5, default=None)
    rating: int | None = Optional[Field(ge=0, le=5)]


class ReviewPatchDto(ReviewPatchRequestDto):
    id: int