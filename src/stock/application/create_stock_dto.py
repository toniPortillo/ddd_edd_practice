from pydantic import BaseModel


class CreateStockDto(BaseModel):
    symbol: str
    name: str
    currency: str
    exchange: str
    mic_code: str
    country: str
    type: str
