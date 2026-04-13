from domain.entities.users import UserDto
from infrastructure.models import UsersOrm
from infrastructure.repositories.mappers.base import BaseDataMapper


class UsersDataMapper(BaseDataMapper):
    db_model = UsersOrm
    schema = UserDto