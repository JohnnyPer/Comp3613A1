from datetime import date

from sqlmodel import SQLModel, Field


class Booking(SQLModel, table=True):
    bookingId: int | None = Field(default=None, primary_key=True)
    startDate: date
    endDate: date
    status: str
    accommodationId: int = Field(foreign_key="accommodation.accommodationId")
    tenantId: int = Field(foreign_key="tenant.tenantId")