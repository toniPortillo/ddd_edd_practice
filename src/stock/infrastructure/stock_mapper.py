from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.config.database import Base


class StockMapper(Base):
    __tablename__ = "stock_stock"

    id = Column(UUID(as_uuid=False), primary_key=True, nullable=False)
    symbol = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    currency = Column(String(), nullable=False)
    exchange = Column(String(), nullable=False)
    mic_code = Column(String(), nullable=False)
    country = Column(String(), nullable=False)
    type = Column(String(), nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Stock(id={self.id}, "
            f"symbol={self.symbol}, "
            f"name={self.name}, "
            f"currency={self.currency}, "
            f"exchange={self.exchange}, "
            f"mic_code={self.mic_code}, "
            f"country={self.country}, "
            f"type={self.type})>"
        )
