from dataclasses import dataclass
import uuid


@dataclass
class Stock:
    stock_id: uuid.UUID
    symbol: str
    name: str
    currency: str
    exchange: str
    mic_code: str
    country: str
    type: str
