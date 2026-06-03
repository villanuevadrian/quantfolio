import uuid
from datetime import date

from sqlalchemy import CheckConstraint, Date, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    mail: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(250), nullable=False)


class Stock(Base):
    __tablename__ = "stock"

    asset_code: Mapped[str] = mapped_column(String(50), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    market: Mapped[str] = mapped_column(String(50), nullable=False)


class Portfolio(Base):
    __tablename__ = "portfolio"

    portfolio_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    asset_type: Mapped[str] = mapped_column(String(50), nullable=False)
    owner: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False
    )

    __table_args__ = (
        CheckConstraint(
            "asset_type IN ('Stock', 'Fund', 'ETF', 'Crypto')",
            name="ck_portfolio_asset_type",
        ),
    )


class Transaction(Base):
    __tablename__ = "transaction"

    transaction_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    asset: Mapped[str] = mapped_column(
        String(50), ForeignKey("stock.asset_code"), nullable=False
    )
    operation_type: Mapped[str] = mapped_column(String(50), nullable=False)
    amount: Mapped[float] = mapped_column(Numeric(15, 4), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(15, 4), nullable=False)
    fee: Mapped[float | None] = mapped_column(Numeric(10, 4), nullable=True)
    platform: Mapped[str] = mapped_column(String(50), nullable=False)
    tx_date: Mapped[date] = mapped_column(Date, nullable=False)
    portfolio: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("portfolio.portfolio_id"), nullable=False
    )

    __table_args__ = (
        CheckConstraint(
            "operation_type IN ('Buy', 'Sell')", name="ck_transaction_operation_type"
        ),
    )


class Event(Base):
    __tablename__ = "event"

    event_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    event_type: Mapped[str] = mapped_column(String(50), nullable=False)
    event_name: Mapped[str] = mapped_column(String(250), nullable=False)
    event_date: Mapped[date] = mapped_column(Date, nullable=False)
    asset: Mapped[str | None] = mapped_column(
        String(50), ForeignKey("stock.asset_code"), nullable=True
    )
    owner: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False
    )
