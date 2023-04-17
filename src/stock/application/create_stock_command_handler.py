from typing import Any, Dict
from stock.domain.stock import Stock
from stock.domain.stock_creator import StockCreator

from stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from stock.application.create_stock_command import CreateStockCommand
from common.infrastructure.client.requests_http_client import RequestsHttpClient


class CreateStockCommandHandler:
    def __init__(
        self,
        stock_repository: SqlalchemyStockRepository,
        stock_creator: StockCreator,
        requests_http_client: RequestsHttpClient,
    ) -> None:
        self.__stock_repository = stock_repository
        self.__stock_creator = stock_creator
        self.__requests_http_client = requests_http_client

    async def handle(
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

        stock_list: Any = self.__requests_http_client.get("/stocks")
        print(stock_list.json())

        self.__stock_repository.save(stock)

        return {
            "id": stock.stock_id,
        }
