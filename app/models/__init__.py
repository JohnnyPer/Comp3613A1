"""Database table models.

Import every table model here so ``SQLModel.metadata.create_all`` sees them.
"""

from app.models.accommodation import Accommodation
from app.models.booking import Booking
from app.models.review import Review
from app.models.tenant import Tenant
from app.models.user import User

__all__ = ["Accommodation", "Booking", "Review", "Tenant", "User"]
