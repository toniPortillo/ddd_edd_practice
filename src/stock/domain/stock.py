from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str
    name: str
    currency: str
    exchange: str
    mic_code: str
    country: str
    type: str
