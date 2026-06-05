from sqlalchemy.orm import Session

from app.models.models import Stock
from app.repositories import stock_repository
from app.schemas.schemas import StockCreate


def get_or_create(db: Session, stock: StockCreate) -> Stock:
    existing = stock_repository.get_by_code(db, stock.asset_code)
    if existing:
        return existing
    return stock_repository.create(db, stock)
