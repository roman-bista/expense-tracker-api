
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from datetime import datetime
from sqlalchemy import func
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        unique=True,
        index=True,
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
    server_default=func.now(),
    nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
    server_default=func.now(),
    onupdate=func.now(),
    nullable=False
    )

    transactions: Mapped[list["Transaction"]] = relationship(
    "Transaction",
    back_populates="user"
    )   


# ✅ Base
# ✅ Mapped
# ✅ mapped_column
# ✅ relationship
# ✅ email
# ✅ hashed_password
# Just ensure the transactions relationship is inside the User class.