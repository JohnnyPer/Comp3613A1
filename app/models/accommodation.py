from decimal import Decimal

from sqlalchemy import Column, Numeric
from sqlmodel import Field, SQLModel


class Accommodation(SQLModel, table=True):
    accommodationId: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=100, index=True)
    description: str = Field(max_length=500)
    monthlyCost: Decimal = Field(
        default=Decimal("0.00"),
        ge=0,
        sa_column=Column(Numeric(10, 2), nullable=False),
    )
    location: str = Field(max_length=100, index=True)
    imageUrl: str = Field(max_length=500, default="")
    ownerId: int = Field(foreign_key="user.id")
    status: str = Field(max_length=20, default="available")  # e.g., available, booked, etc.