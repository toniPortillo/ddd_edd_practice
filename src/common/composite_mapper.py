from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy.orm import CompositeProperty


class CompositeMapper(ABC):
    @abstractmethod
    def composite(self) -> Dict[str, CompositeProperty]:
        pass
