from typing import Type, Dict

from src.stock.domain.stock import Stock
from src.common.mapper import Mapper
from sqlalchemy import Table, Column, String
from sqlalchemy.dialects.postgresql import UUID


class StockMapper(Mapper):
    __table = None

    def table(
        self,
    ) -> Table:
        if self.__table is None:
            self.__table = self.__db_instance.Table(
                "stock_stock",
                Column("id", UUID(as_uuid=False), primary_key=True),
                Column("symbol", String()),
                Column("name", String(), nullable=False),
                Column("currency", String()),
                Column("exchange", String()),
                Column("mic_code", String()),
                Column("country", String()),
                Column("type", String()),
            )
        return self.__table

    def entity(self) -> Type:
        return Stock
