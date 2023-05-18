from typing import Type

from sqlalchemy import Column, String, Table
from sqlalchemy.dialects.postgresql import UUID

from src.common.infrastructure.persistence.mapper import Mapper
from src.stock.domain.stock import Stock

# class StockMapper(Base):
#     __tablename__ = "stock_stock"

#     id = Column(UUID(as_uuid=False), primary_key=True, nullable=False)
#     symbol = Column(String(), nullable=False)
#     name = Column(String(), nullable=False)
#     currency = Column(String(), nullable=False)
#     exchange = Column(String(), nullable=False)
#     mic_code = Column(String(), nullable=False)
#     country = Column(String(), nullable=False)
#     type = Column(String(), nullable=False)

#     def __repr__(self) -> str:
#         return (
#             f"<Stock(id={self.id}, "
#             f"symbol={self.symbol}, "
#             f"name={self.name}, "
#             f"currency={self.currency}, "
#             f"exchange={self.exchange}, "
#             f"mic_code={self.mic_code}, "
#             f"country={self.country}, "
#             f"type={self.type})>"
#         )


class StockMapper(Mapper):
    __table = None

    def table(self) -> Table:
        if self.__table is None:
            self.__table = Table(
                "stock_stock",
                self._db_instance.metadata,
                Column("id", UUID(as_uuid=False), primary_key=True, nullable=False),
                Column("symbol", String(), nullable=False),
                Column("name", String(), nullable=False),
                Column("currency", String(), nullable=False),
                Column("exchjange", String(), nullable=False),
                Column("mic_code", String(), nullable=False),
                Column("country", String(), nullable=False),
                Column("type", String(), nullable=False),
            )

        return self.__table

    def entity(self) -> Type:
        return Stock
