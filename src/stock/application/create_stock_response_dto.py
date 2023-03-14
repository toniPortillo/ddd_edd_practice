from pydantic import BaseModel


class CreateStockResponseDto(BaseModel):
    stock_id: int
    response: str
