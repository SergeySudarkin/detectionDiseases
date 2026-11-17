from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)


class Patient(BaseModel):
    id: int
    name: str
    age: int


@router.get("/", response_model=list[Patient])
async def get_patients():
    return [
        Patient(id=1, name="Пациент 1", age=35),
        Patient(id=2, name="Пациент 2", age=42),
    ]