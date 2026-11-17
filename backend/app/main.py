from fastapi import FastAPI
from app.routers import patients

app = FastAPI(
    title="Detection Diseases API",
    version="1.0.0",
)

app.include_router(patients.router, prefix="/api")


@app.get("/api/health")
async def health():
    return {"status": "ok"}