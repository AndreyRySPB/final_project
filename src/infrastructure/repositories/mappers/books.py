from domain.entities.books import BookDto
from infrastructure.models import BooksOrm
from infrastructure.repositories.mappers.base import BaseDataMapper


class BooksDataMapper(BaseDataMapper):
    db_model = BooksOrm
    schema = BookDto