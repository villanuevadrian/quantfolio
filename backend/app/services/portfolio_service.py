import uuid

from sqlalchemy.orm import Session

from app.models.models import Portfolio
from app.repositories import portfolio_repository
from app.schemas.schemas import PortfolioCreate


def create_portfolio(db: Session, portfolio: PortfolioCreate) -> Portfolio:
    if check_valid_asset(portfolio.asset_type):
        return portfolio_repository.create(db, portfolio)
    raise ValueError(f"Invalid asset_type {portfolio.asset_type}")


# TODO: refactor valid asset types into a shared Enum (single source of truth)
def check_valid_asset(asset_type: str) -> bool:
    return asset_type in ["Stock", "Fund", "ETF", "Crypto"]


def get_portfolio(db: Session, portfolio_id: uuid.UUID) -> Portfolio | None:
    return portfolio_repository.get_by_id(db, portfolio_id)


def get_by_user(db: Session, user_id: uuid.UUID) -> list[Portfolio]:
    return portfolio_repository.get_by_user(db, user_id)
