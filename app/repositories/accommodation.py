from sqlmodel import Session, select

from app.models.accommodation import Accommodation


class AccommodationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, accommodation: Accommodation) -> Accommodation:
        self.db.add(accommodation)
        self.db.commit()
        self.db.refresh(accommodation)
        return accommodation

    def get_by_title(self, title: str) -> Accommodation | None:
        statement = select(Accommodation).where(Accommodation.title == title)
        return self.db.exec(statement).one_or_none()

    def search_by_title_or_location(self, search: str) -> list[Accommodation]:
        statement = select(Accommodation)
        if search.strip():
            pattern = f"%{search.strip()}%"
            statement = statement.where(
                Accommodation.title.ilike(pattern)
                | Accommodation.location.ilike(pattern)
            )
        statement = statement.order_by(Accommodation.accommodationId)
        return list(self.db.exec(statement).all())

    def get_by_id(self, accommodation_id: int) -> Accommodation | None:
        return self.db.get(Accommodation, accommodation_id)