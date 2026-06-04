from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import Stock
from app.schemas.schemas import StockCreate


def get_by_code(db: Session, asset_code: str) -> Stock | None:
    return db.execute(
        select(Stock).where(Stock.asset_code == asset_code)
    ).scalar_one_or_none()


def create(db: Session, stock: StockCreate) -> Stock:
    db_stock = Stock(asset_code=stock.asset_code, name=stock.name, market=stock.market)
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock
