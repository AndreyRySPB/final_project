from datetime import datetime
import typing

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from src.infrastructure.models.base import BaseOrm

if typing.TYPE_CHECKING:
    from infrastructure.models import UsersOrm

class BooksOrm(BaseOrm):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    url_text: Mapped[str] = mapped_column(nullable=True)
    url_cover: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False)

    author: Mapped["UsersOrm"] = relationship("UsersOrm", back_populates="books")
