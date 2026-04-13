from typing import Literal, Optional

from pydantic import BaseModel, EmailStr, Field


class UserRequestAddDto(BaseModel):
    email: EmailStr
    first_name: str | None = Field(min_length=1, max_length=50)
    last_name: str | None = Field(min_length=1, max_length=50)
    password: str = Field(min_length=5, max_length=50)
    role: Literal["reader", "author"]


class UserAddDto(BaseModel):
    email: EmailStr
    first_name: str | None
    last_name: str | None
    role: str
    hashed_password: str
    is_blocked: bool = False


class UserDto(BaseModel):
    id: int
    email: EmailStr
    first_name: str | None
    last_name: str | None
    is_blocked: bool
    role: str


class UserWithHashDto(UserDto):
    hashed_password: str

class UserPatchRequestDto(BaseModel):
    first_name: str | None = Field(min_length=1, max_length=50)
    last_name: str | None = Field(min_length=1, max_length=50)
    is_blocked: bool | None = None
    role: str | None = Optional[Literal["reader", "author"]]

class UserPatchDto(UserPatchRequestDto):
    id: int