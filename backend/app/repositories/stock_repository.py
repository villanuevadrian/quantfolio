from sqlalchemy.orm import Session

from app.models.models import Stock
from app.schemas.schemas import StockCreate


def get_by_code(db: Session, asset_code: str) -> Stock | None:
    return db.query(Stock).filter(Stock.asset_code == asset_code).first()


def create(db: Session, stock: StockCreate) -> Stock:
    db_stock = Stock(asset_code=stock.asset_code, name=stock.name, market=stock.market)
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock
