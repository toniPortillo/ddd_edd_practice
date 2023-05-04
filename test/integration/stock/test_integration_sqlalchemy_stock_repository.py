import pytest
from dependency_injector import providers

from src.stock._dependency_injector.domain.stock_creator_container import StockCreatorContainer
from src.stock._dependency_injector.infrastructure.sqlalchemy_stock_repository_container import (
    SqlalchemyStockRepositoryContainer,
)


@pytest.mark.asyncio
class TestIntegrationSqlAlchemyStockRepository():
    async def test_find_all(self):
        self.fastapi_app
        self.test_client
        sql_alchemy_stock_repository_container = providers.Container(
            SqlalchemyStockRepositoryContainer,
            db_instance=self.database_instance.session,
        )
        stock_creator_container = providers.Container(
            StockCreatorContainer,
        )
        stock_creator = stock_creator_container.stock_creator()
        stock = stock_creator.create(
            symbol="AAPL",
            name="Apple Inc.",
            currency="USD",
            exchange="NASDAQ",
            mic_code="XNAS",
            country="United States",
            type="Common Stock",
        )
        print(stock)

        stock_repository = sql_alchemy_stock_repository_container.sqlalchemy_stock_repository()
        await stock_repository.save(stock)
        stocks = await stock_repository.find_all()
        print(f"stocks: {stocks}")
        assert len(stocks) == 1
