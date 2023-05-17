from uuid import UUID
from typing import List, Optional, Callable, ContextManager

from src.stock.domain.stock import Stock
from src.stock.domain.stock_repository import StockRepository

from sqlalchemy.orm import Session, Query
from src.stock.infrastructure.persistence.stock_mapper import StockMapper


class SqlalchemyStockRepository(StockRepository):
    def __init__(self, db_instance: Callable[..., ContextManager[Session]]) -> None:
        self.__db_instance = db_instance

    async def find_all(self) -> List[Stock]:
        with self.__db_instance() as session:
            query: Query = session.query(StockMapper)
            db_stocks: List[StockMapper] = query.all()
            stocks: List[Stock] = []
            for db_stock in db_stocks:
                stocks.append(
                    Stock(
                        stock_id=UUID(db_stock.id),
                        symbol=db_stock.symbol,
                        name=db_stock.name,
                        currency=db_stock.currency,
                        exchange=db_stock.exchange,
                        mic_code=db_stock.mic_code,
                        country=db_stock.country,
                        type=db_stock.type,
                    )
                )
        return stocks

    async def find_by_id(self, id: UUID) -> Optional[Stock]:
        with self.__db_instance() as session:
            db_stock: Optional[StockMapper] = session.query(StockMapper).get(str(id))
            if db_stock is not None:
                stock: Stock = Stock(
                    stock_id=UUID(db_stock.id),
                    symbol=db_stock.symbol,
                    name=db_stock.name,
                    currency=db_stock.currency,
                    exchange=db_stock.exchange,
                    mic_code=db_stock.mic_code,
                    country=db_stock.country,
                    type=db_stock.type,
                )

        return stock

    async def save(self, stock: Stock) -> None:
        stock_mapper: StockMapper = StockMapper(
            id=str(stock.stock_id),
            symbol=str(stock.symbol),
            name=str(stock.name),
            currency=str(stock.currency),
            exchange=str(stock.exchange),
            mic_code=str(stock.mic_code),
            country=str(stock.country),
            type=str(stock.type),
        )
        with self.__db_instance() as session:
            session.add(stock_mapper)
            session.commit()
            session.refresh(stock_mapper)

    async def save_many(self, stocks: List[Stock]) -> int:
        stocks_mapped: List[StockMapper] = []
        for stock in stocks:
            stock_mapper: StockMapper = StockMapper(
                id=str(stock.stock_id),
                symbol=str(stock.symbol),
                name=str(stock.name),
                currency=str(stock.currency),
                exchange=str(stock.exchange),
                mic_code=str(stock.mic_code),
                country=str(stock.country),
                type=str(stock.type),
            )
            stocks_mapped.append(stock_mapper)

        with self.__db_instance() as session:
            session.add_all(stocks_mapped)
            session.commit()
            return len(stocks_mapped)
