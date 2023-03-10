from dataclasses import dataclass


@dataclass
class Stock:
    stock_id: int
    symbol: str
    name: str
    currency: str
    exchange: str
    mic_code: str
    country: str
    type: str
