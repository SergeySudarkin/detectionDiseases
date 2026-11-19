
import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import (
    UUID,
    JSONB,
    ARRAY,
    ENUM,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import ScreeningLevel


class ScreeningResult(Base):
    __tablename__ = "screening_results"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )

    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("screening_sessions.id"),
        unique=True,
        nullable=False,
    )

    block_scores: Mapped[dict[str, Any]] = mapped_column(
        JSONB,
        nullable=False,
    )

    total_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    red_flag_codes: Mapped[list[str]] = mapped_column(
        ARRAY(Text),
        nullable=False,
        server_default=text("'{}'::text[]"),
    )

    level: Mapped[ScreeningLevel] = mapped_column(
        ENUM(
            ScreeningLevel,
            name="screening_level",
            values_callable=lambda enum: [
                item.value for item in enum
            ],
            create_type=False,
        ),
        nullable=False,
    )

    weights_version: Mapped[str] = mapped_column(
        String(16),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    session: Mapped["ScreeningSession"] = relationship(
        "ScreeningSession",
        back_populates="result",
    )
