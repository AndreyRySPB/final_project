from src.infrastructure.models import UsersOrm
from src.infrastructure.repositories.base import BaseRepository
from src.infrastructure.repositories.mappers.users import UsersDataMapper


class UsersRepository(BaseRepository):
    model = UsersOrm
    mapper = UsersDataMapper