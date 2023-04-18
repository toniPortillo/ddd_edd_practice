from pydantic import BaseModel


class CreateStockResponseDto(BaseModel):
    stocks_from_api: int
    saved_stocks: int
