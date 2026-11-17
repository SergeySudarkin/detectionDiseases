
import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import SessionStatus


class ScreeningSession(Base):
    __tablename__ = "screening_sessions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    session_token: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        default=uuid.uuid4,
    )

    user_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True,
    )

    status: Mapped[SessionStatus] = mapped_column(
        ENUM(
            SessionStatus,
            name="session_status",
            values_callable=lambda enum: [
                item.value for item in enum
            ],
            create_type=False,
        ),
        nullable=False,
        server_default=SessionStatus.IN_PROGRESS.value,
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    answers: Mapped[list["ScreeningAnswer"]] = relationship(
        "ScreeningAnswer",
        back_populates="session",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    result: Mapped["ScreeningResult | None"] = relationship(
        "ScreeningResult",
        back_populates="session",
        uselist=False,
    )
