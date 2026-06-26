import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.schemas import PortfolioCreate, PortfolioResponse
from app.services import portfolio_service

router = APIRouter(prefix="/portfolios", tags=["portfolios"])


@router.post("/", response_model=PortfolioResponse)
def create_portfolio(portfolio: PortfolioCreate, db: Session = Depends(get_db)):
    return portfolio_service.create_portfolio(db, portfolio)


@router.get("/{portfolio_id}", response_model=PortfolioResponse)
def get_portfolio(portfolio_id: uuid.UUID, db: Session = Depends(get_db)):
    portfolio_result = portfolio_service.get_portfolio(db, portfolio_id)
    if portfolio_result is None:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return portfolio_result


@router.get("/", response_model=list[PortfolioResponse])
def list_portfolios(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return portfolio_service.get_by_user(db, user_id)
