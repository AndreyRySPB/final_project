from fastapi import APIRouter

from src.domain.entities.users import UserRequestAddDto
from src.domain.usecases.auth.register_user import RegisterUserUseCase
from src.app.presentation.dependencies.db_manager import DBDep

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", summary="Регистрация пользователя")
async def register_user(
        db: DBDep,
        data: UserRequestAddDto,
):
    return await RegisterUserUseCase().execute(db, data)


@router.post("/login", summary="Вход пользователя")
async def login_user():
    pass


@router.post("/logout", summary="Выход пользователя")
async def logout():
    pass