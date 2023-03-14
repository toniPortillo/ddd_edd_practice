from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy.orm import Session
from sqlalchemy import Table


class Mapper(ABC):
    def __init__(
        self,
        db_instance: Session,
    ) -> None:
        self.__db_instance = db_instance

    @abstractmethod
    def table(self) -> Table:
        pass

    @abstractmethod
    def entity(self) -> Type:
        pass
