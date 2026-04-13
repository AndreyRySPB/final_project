from fastapi import APIRouter

from src.domain.entities.users import UserRequestAddDto
from src.domain.usecases.auth.register_user import RegisterUserUseCase
from src.app.presentation.dependencies.db_manager_dp import DBManagerDep
from src.app.presentation.dependencies.auth_services_dp import AuthServiceDep


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", summary="Регистрация пользователя")
async def register_user(
        db_dp: DBManagerDep,
        auth_dp: AuthServiceDep,
        request_data: UserRequestAddDto,
):
    return await RegisterUserUseCase(db_dp, auth_dp).execute(request_data)


@router.post("/login", summary="Вход пользователя")
async def login_user():
    pass


@router.post("/logout", summary="Выход пользователя")
async def logout():
    pass