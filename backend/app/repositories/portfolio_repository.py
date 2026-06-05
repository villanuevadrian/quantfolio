import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.models import Portfolio
from app.schemas.schemas import PortfolioCreate


def get_by_id(db: Session, portfolio_id: uuid.UUID) -> Portfolio | None:
    return db.execute(
        select(Portfolio).where(Portfolio.portfolio_id == portfolio_id)
    ).scalar_one_or_none()


def get_by_user(db: Session, user_id: uuid.UUID) -> list[Portfolio]:
    return list(db.scalars(select(Portfolio).where(Portfolio.owner == user_id)).all())


def create(db: Session, portfolio: PortfolioCreate) -> Portfolio:
    db_portfolio = Portfolio(
        asset_type=portfolio.asset_type, owner=portfolio.owner, name=portfolio.name
    )
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio
