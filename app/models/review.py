from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Review(SQLModel, table=True):
    accommodationId: int = Field(
        foreign_key="accommodation.accommodationId",
        primary_key=True,
    )
    tenantId: int = Field(
        foreign_key="tenant.tenantId",
        primary_key=True,
    )
    rating: int = Field(ge=1, le=5)
    comment: str = Field(max_length=1000)
    createdOn: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
    )