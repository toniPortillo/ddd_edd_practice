from typing import List
from unittest.mock import Mock
from uuid import UUID

import pytest

from src.stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from src.stock.domain.stock import Stock


@pytest.mark.asyncio
class TestSqlAlchemyStockRepository:
    async def test_find_all(self, query_mock, db_instance_session):
        fake_query_result = [
            {
                "id": "123e4567-e89b-12d3-a456-426655440000",
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "currency": "USD",
                "exchange": "NASDAQ",
                "mic_code": "XNAS",
                "country": "US",
                "type": "equity",
            },
            {
                "id": "223e4567-e89b-12d3-a456-426655440000",
                "symbol": "GOOG",
                "name": "Alphabet Inc.",
                "currency": "USD",
                "exchange": "NASDAQ",
                "mic_code": "XNAS",
                "country": "US",
                "type": "equity",
            },
        ]

        stocks_fake: List[Stock] = []
        for stock_mapper_fake in fake_query_result:
            stocks_fake.append(
                Stock(
                    stock_id=UUID(stock_mapper_fake['id']),
                    symbol=stock_mapper_fake['symbol'],
                    name=stock_mapper_fake['name'],
                    currency=stock_mapper_fake['currency'],
                    exchange=stock_mapper_fake['exchange'],
                    mic_code=stock_mapper_fake['mic_code'],
                    country=stock_mapper_fake['country'],
                    type=stock_mapper_fake['type'],
                )
            )

        query_mock.all.return_value = stocks_fake
        db_instance_session.session_mock.query.return_value = query_mock
        sqlalchemy_stock_repository = SqlalchemyStockRepository(db_instance=db_instance_session)
        stocks = await sqlalchemy_stock_repository.find_all()

        assert len(stocks) == 2
        assert stocks == stocks_fake

    async def test_find_by_id(self, query_mock, db_instance_session):
        fake_query_result = {
            "id": "123e4567-e89b-12d3-a456-426655440000",
            "symbol": "AAPL",
            "name": "Apple Inc.",
            "currency": "USD",
            "exchange": "NASDAQ",
            "mic_code": "XNAS",
            "country": "US",
            "type": "equity",
        }

        stock_fake: Stock = Stock(
            stock_id=UUID(fake_query_result['id']),
            symbol=fake_query_result['symbol'],
            name=fake_query_result['name'],
            currency=fake_query_result['currency'],
            exchange=fake_query_result['exchange'],
            mic_code=fake_query_result['mic_code'],
            country=fake_query_result['country'],
            type=fake_query_result['type'],
        )

        query_mock.get.return_value = stock_fake
        db_instance_session.session_mock.query.return_value = query_mock
        sqlalchemy_stock_repository = SqlalchemyStockRepository(db_instance=db_instance_session)
        stock = await sqlalchemy_stock_repository.find_by_id(id=stock_fake.stock_id)

        assert stock == stock_fake

    async def test_save(self, mocker, db_instance_session):
        stock_fake: Stock = Stock(
            stock_id=UUID("123e4567-e89b-12d3-a456-426655440000"),
            symbol="AAPL",
            name="Apple Inc.",
            currency="USD",
            exchange="NASDAQ",
            mic_code="XNAS",
            country="US",
            type="equity",
        )

        sqlalchemy_stock_repository = SqlalchemyStockRepository(db_instance=db_instance_session)
        await sqlalchemy_stock_repository.save(stock=stock_fake)

        db_instance_session.session_mock.add.assert_called_once_with(stock_fake)
        db_instance_session.session_mock.commit.assert_called_once()
        db_instance_session.session_mock.refresh.assert_called_once_with(stock_fake)

    async def test_save_many(self, mocker, db_instance_session):
        fake_query_result = [
            {
                "id": "123e4567-e89b-12d3-a456-426655440000",
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "currency": "USD",
                "exchange": "NASDAQ",
                "mic_code": "XNAS",
                "country": "US",
                "type": "equity",
            },
            {
                "id": "223e4567-e89b-12d3-a456-426655440000",
                "symbol": "GOOG",
                "name": "Alphabet Inc.",
                "currency": "USD",
                "exchange": "NASDAQ",
                "mic_code": "XNAS",
                "country": "US",
                "type": "equity",
            },
        ]

        stocks_fake: List[Stock] = []
        for fake_result in fake_query_result:
            stocks_fake.append(
                Stock(
                    stock_id=UUID(fake_result["id"]),
                    symbol=fake_result["symbol"],
                    name=fake_result["name"],
                    currency=fake_result["currency"],
                    exchange=fake_result["exchange"],
                    mic_code=fake_result["mic_code"],
                    country=fake_result["country"],
                    type=fake_result["type"],
                )
            )

        sqlalchemy_stock_repository = SqlalchemyStockRepository(db_instance=db_instance_session)
        stocks_saved: int = await sqlalchemy_stock_repository.save_many(stocks=stocks_fake)

        db_instance_session.session_mock.add_all.assert_called_once_with(stocks_fake)
        db_instance_session.session_mock.commit.assert_called_once()
        assert stocks_saved == 2
