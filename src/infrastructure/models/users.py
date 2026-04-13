from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy import Column, Enum
from src.infrastructure.models.base import BaseOrm


class UsersOrm(BaseOrm):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(200))
    is_blocked: Mapped[bool] = mapped_column(default=False)
    role: Mapped[str] = Column(Enum("reader", "author", "admin", name='role_enum'), nullable=False)