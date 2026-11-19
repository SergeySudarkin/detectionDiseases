
import uuid
from datetime import date, datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    LargeBinary,
    SmallInteger,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class SymptomEntry(Base):
    __tablename__ = "symptom_entries"

    __table_args__ = (
        CheckConstraint(
            "pain_vas BETWEEN 0 AND 10",
            name="ck_symptom_entries_pain_vas",
        ),
        CheckConstraint(
            "morning_stiffness_min BETWEEN 0 AND 1440",
            name="ck_symptom_entries_stiffness",
        ),
        CheckConstraint(
            "swollen_joints_selfreport >= 0",
            name="ck_symptom_entries_swollen_joints",
        ),
        CheckConstraint(
            "painful_joints_selfreport >= 0",
            name="ck_symptom_entries_painful_joints",
        ),
        CheckConstraint(
            "fatigue_vas BETWEEN 0 AND 10",
            name="ck_symptom_entries_fatigue_vas",
        ),
        UniqueConstraint(
            "user_id",
            "entry_date",
            name="uq_symptom_entries_user_date",
        ),
    )

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

    entry_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    pain_vas: Mapped[int | None] = mapped_column(
        SmallInteger,
    )

    morning_stiffness_min: Mapped[int | None] = mapped_column(
        SmallInteger,
    )

    swollen_joints_selfreport: Mapped[int | None] = mapped_column(
        SmallInteger,
    )

    painful_joints_selfreport: Mapped[int | None] = mapped_column(
        SmallInteger,
    )

    fatigue_vas: Mapped[int | None] = mapped_column(
        SmallInteger,
    )

    flares: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="false",
    )

    notes_enc: Mapped[bytes | None] = mapped_column(
        LargeBinary,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    user: Mapped["User"] = relationship("User")
