from sqlmodel import Session, select

from app.models.review import Review


class ReviewRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_for_accommodation(self, accommodation_id: int) -> list[Review]:
        statement = select(Review).where(
            Review.accommodationId == accommodation_id
        ).order_by(Review.createdOn.desc())

        return list(self.db.exec(statement).all())