from fastapi import APIRouter



router = APIRouter(prefix="/reviews", tags=["Комментарии"])


@router.get("/books", summary="Получить все комментарии по книгам")
async def get_all_reviews():
    pass

@router.get("books/{book_id}/", summary="Получить все комментарии к книге")
async def get_all_reviews_to_book():
    pass

@router.post("/{review_id}/", summary="Получить комментарий")
async def get_review():
    pass

@router.post("/users/{user_id}/", summary="Получить все комментарии пользователя")
async def get_reviews_by_user_id():
    pass


@router.post("/books/{book_id}/", summary="Создать комментарий к книге")
async def create_review_to_book():
    pass


@router.patch("/{review_id}", summary="Обновить комментарий к книге")
async def update_review_to_book():
    pass


@router.delete("/{review_id}", summary="Удалить комментарий к книге")
async def update_review_to_book():
    pass