from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", summary="Получить всех пользователей")
async def get_all_users():
    pass


@router.get("/me", summary="Получить инфу о себе")
async def get_me():
    pass


@router.get("/{user_id}", summary="Получить инфу о пользователе")
async def get_me():
    pass


@router.patch("/{user_id}", summary="Обновить пользователя")
async def update_user_info():
    pass


@router.delete("/{user_id}", summary="Удалить пользователя")
async def delete_user():
    pass