
import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    SmallInteger,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import Sex


class PatientProfile(Base):
    __tablename__ = "patient_profiles"

    __table_args__ = (
        CheckConstraint(
            "year_of_birth BETWEEN 1920 AND 2025",
            name="check_year_of_birth",
        ),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )

    year_of_birth: Mapped[int | None] = mapped_column(
        SmallInteger,
        nullable=True,
    )

    sex: Mapped[Sex | None] = mapped_column(
        ENUM(
            Sex,
            name="sex",
            values_callable=lambda enum: [
                item.value for item in enum
            ],
            create_type=False,
        ),
        nullable=True,
    )

    diagnosis_code: Mapped[str | None] = mapped_column(
        String(8),
        nullable=True,
    )

    diagnosis_confirmed_by_doctor: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="false",
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="patient_profile",
    )
