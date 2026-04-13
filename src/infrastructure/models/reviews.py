from datetime import datetime
import typing

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Column, Integer, CheckConstraint
from src.infrastructure.models.base import BaseOrm

if typing.TYPE_CHECKING:
    from src.infrastructure.models import UsersOrm, BooksOrm


class ReviewsOrm(BaseOrm):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[int] = Column(
        Integer,
        CheckConstraint('rating >= 0 AND rating <= 5', name='rating_check'),
        default=0,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(nullable=False)

    author: Mapped["UsersOrm"] = relationship("UsersOrm", back_populates="reviews")
    book: Mapped["BooksOrm"] = relationship("BooksOrm", back_populates="reviews")
