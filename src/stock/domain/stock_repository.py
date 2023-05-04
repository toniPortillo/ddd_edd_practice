from abc import ABC, abstractmethod
from typing import List, Optional

from src.stock.domain.stock import Stock


class StockRepository(ABC):
    @abstractmethod
    async def find_all(self) -> List[Stock]:
        pass

    @abstractmethod
    async def find_by_id(self, id: int) -> Optional[Stock]:
        pass

    @abstractmethod
    async def save(self, stock: Stock) -> None:
        pass

    @abstractmethod
    async def save_many(self, stocks: List[Stock]) -> int:
        pass
