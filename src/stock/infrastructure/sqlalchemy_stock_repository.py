from typing import Optional

from src.stock.domain.stock import Stock
from src.stock.domain.stock_repository import StockRepository

from sqlalchemy.orm import Session


class SqlalchemyStockRepository(StockRepository):
    def __init__(
        self,
        db_instance: Session
    ) -> None:
        self.__db_instance = db_instance

    def find_by_id(
        self, 
        id: int
    ) -> Optional[Stock]:
        pass

    def save(
        self, 
        stock: Stock
    ) -> None:
        self.__db_instance.stock.merge(stock)
