
import uuid
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    DateTime,
    ForeignKey,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import ReminderType


class Reminder(Base):
    __tablename__ = "reminders"

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

    type: Mapped[ReminderType] = mapped_column(
        ENUM(
            ReminderType,
            name="reminder_type",
            values_callable=lambda enum: [
                item.value for item in enum
            ],
            create_type=False,
        ),
        nullable=False,
    )

    related_id: Mapped[int | None] = mapped_column(
        BigInteger,
    )

    scheduled_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    sent_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    status: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        server_default="pending",
    )

    user: Mapped["User"] = relationship("User")
