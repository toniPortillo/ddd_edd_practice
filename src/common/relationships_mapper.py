from abc import ABC, abstractmethod
from typing import Dict

from sqlalchemy.orm import RelationshipProperty


class RelasionshipsMapper(ABC):
    @abstractmethod
    def relationships(self) -> Dict[str, RelationshipProperty]:
        pass
