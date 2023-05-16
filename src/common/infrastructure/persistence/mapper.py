from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy import Table

from app.config.database import Database


class Mapper(ABC):
    def __init__(self, db_instance: Database) -> None:
        self._db_instance = db_instance

    @abstractmethod
    def table(self) -> Table:
        ...

    @abstractmethod
    def entity(self) -> Type:
        ...
