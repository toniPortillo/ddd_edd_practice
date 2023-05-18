from uuid import UUID
from typing import List, Optional, Callable, ContextManager

from src.stock.domain.stock import Stock
from src.stock.domain.stock_repository import StockRepository

from sqlalchemy.orm import Session, Query


class SqlalchemyStockRepository(StockRepository):
    def __init__(self, db_instance: Callable[..., ContextManager[Session]]) -> None:
        self.__db_instance = db_instance

    async def find_all(self) -> List[Stock]:
        with self.__db_instance() as session:
            query: Query = session.query(Stock)
            stocks: List[Stock] = query.all()

            return stocks

    async def find_by_id(self, id: UUID) -> Optional[Stock]:
        with self.__db_instance() as session:
            stock: Optional[Stock] = session.query(Stock).get(str(id))

            return stock

    async def save(self, stock: Stock) -> None:
        with self.__db_instance() as session:
            session.add(stock)
            session.commit()
            session.refresh(stock)

    async def save_many(self, stocks: List[Stock]) -> int:
        with self.__db_instance() as session:
            session.add_all(stocks)
            session.commit()
            return len(stocks)
