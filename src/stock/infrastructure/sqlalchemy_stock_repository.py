from typing import List, Optional, Callable, ContextManager

from src.stock.domain.stock import Stock
from src.stock.domain.stock_repository import StockRepository

from sqlalchemy.orm import Session
from src.stock.infrastructure.stock_mapper import StockMapper


class SqlalchemyStockRepository(StockRepository):
    def __init__(self, db_instance: Callable[..., ContextManager[Session]]) -> None:
        self.__db_instance = db_instance

    async def find_by_id(self, id: int) -> Optional[Stock]:
        pass

    async def save(self, stock: Stock) -> None:
        stock_mapper: StockMapper = StockMapper(
            id=stock.stock_id,
            symbol=stock.symbol,
            name=stock.name,
            currency=stock.currency,
            exchange=stock.exchange,
            mic_code=stock.mic_code,
            country=stock.country,
            type=stock.type,
        )
        with self.__db_instance() as session:
            session.add(stock_mapper)
            session.commit()
            session.refresh(stock_mapper)

    async def save_many(self, stocks: List[Stock]) -> int:
        stocks_mapped: List[StockMapper] = []
        for stock in stocks:
            stock_mapper: StockMapper = StockMapper(
                id=stock.stock_id,
                symbol=stock.symbol,
                name=stock.name,
                currency=stock.currency,
                exchange=stock.exchange,
                mic_code=stock.mic_code,
                country=stock.country,
                type=stock.type,
            )
            stocks_mapped.append(stock_mapper)

        with self.__db_instance() as session:
            session.add_all(stocks_mapped)
            session.commit()
            return len(stocks_mapped)
