
import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from sqlalchemy import (
    BigInteger,
    Date,
    DateTime,
    ForeignKey,
    Numeric,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import DataSource


class LabResult(Base):
    __tablename__ = "lab_results"

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

    test_code: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    value: Mapped[Decimal] = mapped_column(
        Numeric,
        nullable=False,
    )

    unit: Mapped[str | None] = mapped_column(
        Text,
    )

    lab_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    reference_range: Mapped[dict[str, Any] | None] = mapped_column(
        JSONB,
    )

    entered_by: Mapped[DataSource] = mapped_column(
        ENUM(
            DataSource,
            name="data_source",
            values_callable=lambda enum: [
                item.value for item in enum
            ],
            create_type=False,
        ),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    user: Mapped["User"] = relationship("User")
