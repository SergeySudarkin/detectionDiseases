
import uuid
from datetime import date, datetime

from sqlalchemy import (
    BigInteger,
    Date,
    DateTime,
    ForeignKey,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import IntakeStatus


class MedicationIntakeLog(Base):
    __tablename__ = "medication_intake_log"

    __table_args__ = (
        UniqueConstraint(
            "medication_id",
            "scheduled_date",
            name="uq_medication_intake_date",
        ),
    )

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    medication_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("medications.id", ondelete="CASCADE"),
        nullable=False,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    scheduled_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    taken_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    status: Mapped[IntakeStatus] = mapped_column(
        ENUM(
            IntakeStatus,
            name="intake_status",
            values_callable=lambda enum: [
                item.value for item in enum
            ],
            create_type=False,
        ),
        nullable=False,
    )

    reason_skipped: Mapped[str | None] = mapped_column(
        Text,
    )

    medication: Mapped["Medication"] = relationship(
        "Medication",
        back_populates="intake_logs",
    )

    user: Mapped["User"] = relationship("User")
