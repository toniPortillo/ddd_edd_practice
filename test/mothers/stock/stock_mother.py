from src.stock.domain.stock import Stock
from src.stock.domain.stock_creator import StockCreator


class StockMother:
    @staticmethod
    def apple_stock() -> Stock:
        apple_stock = StockCreator.create(
            symbol="AAPL",
            name="Apple Inc.",
            currency="USD",
            exchange="NASDAQ",
            mic_code="XNAS",
            country="United States",
            type="Common Stock",
        )

        return apple_stock

    @staticmethod
    def millennium_stock() -> Stock:
        millennium_stock = StockCreator.create(
            symbol="MSC",
            name="Studio City International Holdings Ltd",
            currency="USD",
            exchange="NYSE",
            mic_code="XNYS",
            country="United States",
            type="Depositary Receipt",
        )

        return millennium_stock
