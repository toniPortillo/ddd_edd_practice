from abc import ABC, abstractmethod
from typing import Optional

from src.stock.domain.stock import Stock

class StockRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Stock]:
        pass

    @abstractmethod
    def save(self, stock: Stock) -> None:
        pass
