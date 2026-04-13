from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["Книги"])


@router.get("", summary="Получить все книги")
async def get_all_books():
    pass


@router.get("/{book_id}", summary="Получить книгу")
async def get_book():
    pass


@router.post("", summary="Создать книгу")
async def create_book():
    pass


@router.patch("/{book_id}", summary="Изменить книгу")
async def partially_update_book():
    pass


@router.delete("/{book_id}", summary="Удалить книгу")
async def delete_book():
    pass


@router.post("/{book_id}/book_file", summary="Загрузить файл книги")
async def add_book_file():
    pass


@router.delete("/{book_id}/book_file", summary="Удалить файл книги")
async def delete_book_file():
    pass


@router.post("/{book_id}/cover_file", summary="Загрузить обложку книги")
async def add_book_cover():
    pass


@router.delete("/{book_id}/cover_file", summary="Удалить обложку книги")
async def delete_book_cover():
    pass


@router.get("/authors", summary="Получить все книги автора")
async def get_all_books_by_author_id():
    pass


@router.get("/authors/{author_id}", summary="Получить все книги автора")
async def get_all_books_by_author_id():
    pass