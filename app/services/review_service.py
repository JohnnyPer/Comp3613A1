from app.models.review import Review
from app.repositories.review import ReviewRepository


class ReviewService:
    def __init__(self, repository: ReviewRepository):
        self.repository = repository

    def get_reviews_for_accommodation(
        self, accommodation_id: int
    ) -> list[Review]:
        return self.repository.list_for_accommodation(accommodation_id)

    def get_average_rating(self, reviews: list[Review]) -> float | None:
        if not reviews:
            return None

        return sum(review.rating for review in reviews) / len(reviews)