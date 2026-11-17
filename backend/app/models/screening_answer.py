
import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import (
    BigInteger,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class ScreeningAnswer(Base):
    __tablename__ = "screening_answers"

    __table_args__ = (
        UniqueConstraint(
            "session_id",
            "question_code",
            name="uq_screening_answers_session_question",
        ),
    )

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "screening_sessions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    question_code: Mapped[str] = mapped_column(
        String(8),
        nullable=False,
    )

    value: Mapped[Any] = mapped_column(
        JSONB,
        nullable=False,
    )

    weighted_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    session: Mapped["ScreeningSession"] = relationship(
        "ScreeningSession",
        back_populates="answers",
    )
