from typing import Dict
from src.stock.domain.stock import Stock
from src.stock.domain.stock_creator import StockCreator

from src.stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from src.stock.application.create_stock_command import CreateStockCommand


class CreateStockCommandHandler:
    def __init__(
        self,
        stock_repository: SqlalchemyStockRepository,
        stock_creator: StockCreator,
    ) -> None:
        self.__stock_repository = stock_repository
        self.__stock_creator = stock_creator

    def handle(
        self,
        command: CreateStockCommand,
    ) -> Dict:
        stock: Stock = self.__stock_creator.create(
            symbol=command.symbol,
            name=command.name,
            currency=command.currency,
            exchange=command.exchange,
            mic_code=command.mic_code,
            country=command.country,
            type=command.type,
        )

        self.__stock_repository.save(stock)

        return {
            "id": stock.stock_id,
        }
