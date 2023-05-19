from typing import List
import pytest
from stock.domain.stock import Stock

from test.mothers.stock.stock_mother import StockMother

@pytest.mark.asyncio
class TestIntegrationSqlAlchemyStockRepository():
    async def test_find_all(self, sqlalchemy_stock_repository):
        stock_list: List[Stock] = [
            StockMother.apple_stock(),
            StockMother.millennium_stock(),
        ]
        await sqlalchemy_stock_repository.save_many(stock_list)
        stocks = await sqlalchemy_stock_repository.find_all()

        assert stocks == stock_list

    async def test_save(self, sqlalchemy_stock_repository):
        stock: Stock = StockMother.apple_stock()
        await sqlalchemy_stock_repository.save(stock)
        db_stock: Stock = await sqlalchemy_stock_repository.find_by_id(stock.id)

        assert stock == db_stock
