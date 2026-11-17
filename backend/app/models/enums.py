
from enum import Enum


class UserRole(str, Enum):
    PATIENT = "patient"
    ADMIN = "admin"
    MEDICAL_REVIEWER = "medical_reviewer"


class Sex(str, Enum):
    MALE = "male"
    FEMALE = "female"
    UNDISCLOSED = "undisclosed"


class SessionStatus(str, Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ABANDONED = "abandoned"


class ScreeningLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    RED_FLAG = "red_flag"


class IntakeStatus(str, Enum):
    TAKEN = "taken"
    SKIPPED = "skipped"
    DELAYED = "delayed"


class DataSource(str, Enum):
    PATIENT = "patient"
    DOCTOR = "doctor"


class ReviewStatus(str, Enum):
    DRAFT = "draft"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    PUBLISHED = "published"


class ReminderType(str, Enum):
    MEDICATION = "medication"
    VISIT = "visit"
    LAB = "lab"


class AuditAction(str, Enum):
    READ = "read"
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    EXPORT = "export"
