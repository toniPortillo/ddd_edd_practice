from typing import Type

from src.stock.domain.stock import Stock
from src.common.mapper import Mapper
from sqlalchemy import Table, Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.config.database import Base


class StockMapper(Base):
    __tablename__ = "stock_stock"

    id = Column(UUID(as_uuid=False), primary_key=True)
    symbol = Column(String())
    name = Column(String(), nullable=False)
    currency = Column(String())
    exchange = Column(String())
    mic_code = Column(String())
    country = Column(String())
    type = Column(String())

    def __repr__(self):
        return f"<Stock(id={self.id}, "\
            f"symbol={self.symbol}, "\
            f"name={self.name}, "\
            f"currency={self.currency}, "\
            f"exchange={self.exchange}, "\
            f"mic_code={self.mic_code}, "\
            f"country={self.country}, "\
            f"type={self.type})>"
