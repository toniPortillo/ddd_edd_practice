from typing import Optional, Callable, ContextManager

from src.stock.domain.stock import Stock
from src.stock.domain.stock_repository import StockRepository

from sqlalchemy.orm import Session
from src.stock.infrastructure.stock_mapper import StockMapper


class SqlalchemyStockRepository(StockRepository):
    def __init__(self, db_instance: Callable[..., ContextManager[Session]]) -> None:
        self.__db_instance = db_instance

    def find_by_id(self, id: int) -> Optional[Stock]:
        pass

    def save(self, stock: Stock) -> None:
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
