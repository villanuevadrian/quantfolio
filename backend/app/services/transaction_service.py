from sqlalchemy.orm import Session

from app.models.models import Transaction
from app.repositories import (
    portfolio_repository,
    stock_repository,
    transaction_repository,
)
from app.schemas.schemas import TransactionCreate


def create_transaction(db: Session, transaction: TransactionCreate) -> Transaction:
    if portfolio_repository.get_by_id(db, transaction.portfolio) is None:
        raise ValueError(f"Portfolio {transaction.portfolio} does not exist")
    if stock_repository.get_by_code(db, transaction.asset) is None:
        raise ValueError(f"Stock {transaction.asset} does not exist")
    return transaction_repository.create(db, transaction)
