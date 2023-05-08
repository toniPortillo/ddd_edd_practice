import pytest

from src.stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository



@pytest.mark.asyncio
class TestSqlAlchemyStockRepository:
    async def test_find_all(self, db_instance_session):
        sqlalchemy_stock_repository = SqlalchemyStockRepository(db_instance=db_instance_session)
        stocks = await sqlalchemy_stock_repository.find_all()

        assert len(stocks) == 2

    