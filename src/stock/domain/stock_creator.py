from uuid import uuid4
from src.stock.domain.stock import Stock


class StockCreator:
    @classmethod
    def create(
        self, symbol: str, name: str, currency: str, exchange: str, mic_code: str, country: str, type: str
    ) -> Stock:
        stock: Stock = Stock(
            id=uuid4(),
            symbol=symbol,
            name=name,
            currency=currency,
            exchange=exchange,
            mic_code=mic_code,
            country=country,
            type=type,
        )

        return stock
