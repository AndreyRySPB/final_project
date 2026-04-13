from infrastructure.managers.db_manager import DBManager
from src.infrastructure.services.auth import AuthService
from src.domain.entities.users import UserRequestAddDto, UserAddDto


class RegisterUserUseCase:
    def __init__(self, db_manager: DBManager, auth_service: AuthService):
        self.db_manager = db_manager
        self.auth_service = auth_service

    async def execute(self, user_data: UserRequestAddDto):
        hashed_password = self.auth_service.hash_password(password=user_data.password)
        _data = UserAddDto(
            email=user_data.email,
            role=user_data.role,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            hashed_password=hashed_password,
            is_blocked=False
        )
        res = await self.db_manager.users.add(_data)
        await self.db_manager.commit()
        return res