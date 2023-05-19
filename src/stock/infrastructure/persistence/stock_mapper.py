from typing import Type

from sqlalchemy import Column, String, Table
from sqlalchemy.dialects.postgresql import UUID

from src.common.infrastructure.persistence.mapper import Mapper
from src.stock.domain.stock import Stock


class StockMapper(Mapper):
    __table = None

    def table(self) -> Table:
        if self.__table is None:
            self.__table = Table(
                "stock_stock",
                self._db_instance.metadata,
                Column("id", UUID(as_uuid=True), primary_key=True, nullable=False),
                Column("symbol", String(), nullable=False),
                Column("name", String(), nullable=False),
                Column("currency", String(), nullable=False),
                Column("exchange", String(), nullable=False),
                Column("mic_code", String(), nullable=False),
                Column("country", String(), nullable=False),
                Column("type", String(), nullable=False),
            )

        return self.__table

    def entity(self) -> Type:
        return Stock
