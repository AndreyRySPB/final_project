from domain.entities.reviews import ReviewDto
from infrastructure.models.reviews import ReviewsOrm
from infrastructure.repositories.mappers.base import BaseDataMapper


class ReviewsDataMapper(BaseDataMapper):
    db_model = ReviewsOrm
    schema = ReviewDto