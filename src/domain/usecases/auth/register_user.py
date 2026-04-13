from infrastructure.managers.db_manager import DBManager
from src.infrastructure.services.auth import AuthService
from src.domain.entities.users import UserRequestAddDto, UserAddDto


class RegisterUserUseCase:
    @classmethod
    async def execute(cls, db: DBManager, data: UserRequestAddDto):
        hashed_password = AuthService().hash_password(password=data.password)
        _data = UserAddDto(
            email=data.email,
            role=data.role,
            first_name=data.first_name,
            last_name=data.last_name,
            hashed_password=hashed_password,
            is_blocked=False
        )
        res = await db.users.add(_data)
        await db.commit()
        return res