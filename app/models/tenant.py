from sqlmodel import Field, SQLModel


class Tenant(SQLModel, table=True):
    tenantId: int | None = Field(default=None, primary_key=True)
    userId: int = Field(foreign_key="user.id", unique=True)
    name: str = Field(max_length=100)
    email: str = Field(max_length=254)
    phone: str = Field(max_length=30)
    status: str = Field(max_length=20, default="active")
