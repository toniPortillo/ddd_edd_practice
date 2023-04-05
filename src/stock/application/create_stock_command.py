from dataclasses import dataclass


@dataclass(frozen=True)
class CreateStockCommand:
    symbol: str
    name: str
    currency: str
    exchange: str
    mic_code: str
    country: str
    type: str
