import pytest


@pytest.mark.asyncio
class TestIntegrationSqlAlchemyStockRepository():
    async def test_find_all(self, stock_creator, sqlalchemy_stock_repository):
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

        await sqlalchemy_stock_repository.save(stock)
        stocks = await sqlalchemy_stock_repository.find_all()
        print(f"stocks: {stocks}")
        assert len(stocks) == 1

    async def test_save(self):
        pass
