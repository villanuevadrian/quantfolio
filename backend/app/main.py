from fastapi import FastAPI
from app.database import engine, Base
import app.models.models # noqa: F401 — needed so Base knows about the models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "QuantFolio",
    description = "Personal investment portfolio tracker",
    version = "0.1.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}