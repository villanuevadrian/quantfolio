from sqlalchemy.orm import Session

from app.models.models import Portfolio
from app.repositories import portfolio_repository
from app.schemas.schemas import PortfolioCreate


def create_portfolio(db: Session, portfolio: PortfolioCreate) -> Portfolio:
    if check_valid_asset(portfolio.asset_type):
        return portfolio_repository.create(db, portfolio)
    raise ValueError(f"Invalid asset_type {portfolio.asset_type}")


def check_valid_asset(asset_type: str) -> bool:
    return asset_type in ["Stock", "Fund", "ETF", "Crypto"]
