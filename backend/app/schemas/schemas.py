import uuid
from datetime import date

from pydantic import BaseModel


class StockCreate(BaseModel):
    """Schema for creating a new stock in the catalogue."""

    asset_code: str
    name: str
    market: str


class StockResponse(StockCreate):
    """Schema for returning a stock from the API."""

    class Config:
        from_attributes = True


class PortfolioCreate(BaseModel):
    """Schema for creating a new portfolio."""

    asset_type: str
    owner: uuid.UUID
    name: str


class PortfolioResponse(PortfolioCreate):
    """Schema for returning a portfolio from the API."""

    portfolio_id: uuid.UUID

    class Config:
        from_attributes = True


class TransactionCreate(BaseModel):
    """Schema for creating a new transaction."""

    asset: str
    operation_type: str
    amount: float
    price: float
    fee: float | None
    platform: str
    tx_date: date
    portfolio: uuid.UUID


class TransactionResponse(TransactionCreate):
    """Schema for returning a transaction from the API."""

    transaction_id: uuid.UUID

    class Config:
        from_attributes = True
