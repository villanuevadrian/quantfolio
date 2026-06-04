import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import Transaction
from app.schemas.schemas import TransactionCreate


def get_by_id(db: Session, transaction_id: uuid.UUID) -> Transaction | None:
    return db.execute(
        select(Transaction).where(Transaction.transaction_id == transaction_id)
    ).scalar_one_or_none()


def get_by_portfolio(db: Session, portfolio_id: uuid.UUID) -> list[Transaction]:
    return list(
        db.scalars(
            select(Transaction).where(Transaction.portfolio == portfolio_id)
        ).all()
    )


def create(db: Session, transaction: TransactionCreate) -> Transaction:
    db_transaction = Transaction(
        asset=transaction.asset,
        operation_type=transaction.operation_type,
        amount=transaction.amount,
        price=transaction.price,
        fee=transaction.fee,
        platform=transaction.platform,
        tx_date=transaction.tx_date,
        portfolio=transaction.portfolio,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
