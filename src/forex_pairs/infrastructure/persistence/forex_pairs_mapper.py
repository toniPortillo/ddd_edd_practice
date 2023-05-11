from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.config.database import Base


class ForexPairsMapper(Base):
    __tablename__ = "forex_pairs"

    id = Column(UUID(as_uuid=False), primary_key=True, nullable=False)
    symbol = Column(String(), nullable=False)
    currency_group = Column(String(), nullable=False)
    currency_base = Column(String(), nullable=False)
    currency_quote = Column(String(), nullable=False)
