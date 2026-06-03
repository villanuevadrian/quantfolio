from fastapi import FastAPI

import app.models.models  # noqa: F401 — needed so Base knows about the models
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="QuantFolio",
    description="Personal investment portfolio tracker",
    version="0.1.0",
)


@app.get("/health")  # type: ignore[attr-defined]
def health_check():
    return {"status": "ok"}
