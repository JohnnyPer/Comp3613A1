from app.models.accommodation import Accommodation
from app.repositories.accommodation import AccommodationRepository


class AccommodationService:
    def __init__(self, accommodation_repo: AccommodationRepository):
        self.accommodation_repo = accommodation_repo

    def search_listings(self, search: str) -> list[Accommodation]:
        return self.accommodation_repo.search_by_title_or_location(search)

    def get_listing(self, accommodation_id: int) -> Accommodation | None:
        return self.accommodation_repo.get_by_id(accommodation_id)
