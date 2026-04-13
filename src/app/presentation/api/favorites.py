from fastapi import APIRouter

from domain.usecases.favorites.delete_book_from_my_favorites import DeleteBookFromMyFavoritesUseCase
from domain.usecases.favorites.get_my_favorites_books import GetMyFavoritesBooksUseCase
from domain.usecases.favorites.add_book_to_my_favorites import AddBookToMyFavoritesUseCase


router = APIRouter(prefix="/favorites", tags=["Избранное"])


@router.get("/books/me", summary="Получить все избранные книги")
async def get_all_my_favorites_books():
    return await GetMyFavoritesBooksUseCase().execute()


@router.post("/books/{book_id}", summary="Добавить в избранное книгу")
async def add_book_to_my_favorites():
    return await AddBookToMyFavoritesUseCase().execute()


@router.delete("/books/{book_id}", summary="Удалить из избранного книгу")
async def delete_book_from_my_favorites():
    return await DeleteBookFromMyFavoritesUseCase().execute()
