from sqlmodel import Session, select, func

from app.models.tenant import Tenant
from app.models.booking import Booking
from app.models.accommodation import Accommodation


class TenantDirectoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def search_directory(self, search: str) -> list[tuple[Tenant, str | None]]:
            statement = (
                select(Tenant, Accommodation.title)
                .outerjoin(
                    Booking,
                    (Booking.tenantId == Tenant.tenantId)
                    & (Booking.status == "active")
                )
                .outerjoin(
                    Accommodation,
                    Accommodation.accommodationId == Booking.accommodationId
                )
                .where(
                    (Tenant.name.ilike(f"%{search}%"))
                    | (Tenant.email.ilike(f"%{search}%"))
                    | (Tenant.phone.ilike(f"%{search}%"))
                )
            )

            return list(self.db.exec(statement).all())

    def count_all(self) -> int:
        statement = select(func.count()).select_from(Tenant)
        return self.db.exec(statement).one()

    def count_active(self) -> int:
        statement = (
            select(func.count())
            .select_from(Tenant)
            .where(Tenant.status == "active")
        )
        return self.db.exec(statement).one()