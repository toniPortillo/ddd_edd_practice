from typing import Dict, List

from requests import Response
from src.stock.infrastructure.api.controller.stock_json_schema_validator import StockJsonSchemaValidator

from stock.domain.stock import Stock
from stock.domain.stock_creator import StockCreator

from stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from common.infrastructure.client.requests_http_client import RequestsHttpClient


class CreateStockCommandHandler:
    def __init__(
        self,
        stock_repository: SqlalchemyStockRepository,
        stock_creator: StockCreator,
        requests_http_client: RequestsHttpClient,
        stock_json_schema_validator: StockJsonSchemaValidator,
    ) -> None:
        self.__stock_repository = stock_repository
        self.__stock_creator = stock_creator
        self.__requests_http_client = requests_http_client
        self.__stock_json_schema_validator = stock_json_schema_validator

    async def handle(
        self,
    ) -> Dict:
        stock_response: Response = await self.__requests_http_client.get("/stocks")
        stock_list: Dict = stock_response.json()
        stocks_from_api: int = len(stock_list["data"])
        await self.__stock_json_schema_validator.validate(stock_list)

        stocks: List[Stock] = []
        for stock in stock_list["data"]:
            stocks.append(
                self.__stock_creator.create(
                    symbol=stock.get("symbol"),
                    name=stock.get("name"),
                    currency=stock.get("currency"),
                    exchange=stock.get("exchange"),
                    mic_code=stock.get("mic_code"),
                    country=stock.get("country"),
                    type=stock.get("type"),
                )
            )
        saved_stocks: int = await self.__stock_repository.save_many(stocks)

        return {"stocks_from_api": stocks_from_api, "saved_stocks": saved_stocks}
