
import uuid
from datetime import date, datetime
from typing import Any

from sqlalchemy import (
    BigInteger,
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Medication(Base):
    __tablename__ = "medications"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    dose: Mapped[str | None] = mapped_column(
        Text,
    )

    schedule: Mapped[dict[str, Any]] = mapped_column(
        JSONB,
        nullable=False,
    )

    start_date: Mapped[date | None] = mapped_column(
        Date,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="true",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    user: Mapped["User"] = relationship("User")

    intake_logs: Mapped[list["MedicationIntakeLog"]] = relationship(
        "MedicationIntakeLog",
        back_populates="medication",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
