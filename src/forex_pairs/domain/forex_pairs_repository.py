from abc import ABC, abstractmethod
from typing import List

from forex_pairs.domain.forex_pairs import ForexPairs


class ForexPairsRepository(ABC):
    @abstractmethod
    async def save_many(self, forex_pairs: List[ForexPairs]) -> int:
        ...
