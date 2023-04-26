import jsonschema
import pytest
from unittest import TestCase
from unittest.mock import Mock, AsyncMock

from stock.application.create_stock_command_handler import CreateStockCommandHandler
from stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from stock.infrastructure.api.controller.stock_json_schema_validator import StockJsonSchemaValidator
from stock.domain.stock_creator import StockCreator
from common.infrastructure.client.requests_http_client import RequestsHttpClient


class TestCreateStockCommandHandler(TestCase):
    def setUp(self) -> None:
        self.stock_repository_mock = AsyncMock(SqlalchemyStockRepository)
        self.stock_creator_mock = StockCreator()
        self.requests_http_client_mock = AsyncMock(RequestsHttpClient)
        self.stock_json_schema_validator_mock = AsyncMock(StockJsonSchemaValidator)
        self.command_handler = CreateStockCommandHandler(
            stock_repository=self.stock_repository_mock,
            stock_creator=self.stock_creator_mock,
            requests_http_client=self.requests_http_client_mock,
            stock_json_schema_validator=self.stock_json_schema_validator_mock,
        )

    @pytest.mark.asyncio
    async def test_handle(self) -> None:
        
        response_data = {
            "data": [
                {
                    "symbol": "TCS",
                    "name": "Tata Consultancy Services Limited",
                    "currency": "INR",
                    "exchange": "NSE",
                    "mic_code": "XNSE",
                    "country": "India",
                    "type": "Common Stock",
                    "access": {
                        "global": "Level A",
                        "plan": "Grow"
                    }
                },
                {
                    "symbol": "TCS",
                    "name": "Axon Enterprise Inc",
                    "currency": "EUR",
                    "exchange": "FSX",
                    "mic_code": "XFRA",
                    "country": "Germany",
                    "type": "Common Stock",
                    "access": {
                        "global": "Level A",
                        "plan": "Grow"
                    }
                },
                {...}
            ],
            "status": "ok"
        }

        mock_response = Mock()
        mock_response.json.return_value = response_data
        self.requests_http_client_mock.get.return_value = mock_response
        self.stock_json_schema_validator_mock.validate.return_value = None
        self.stock_repository_mock.save_many.return_value = 2
        result = await self.command_handler.handle()
        assert result == {"stocks_from_api": 2, "saved_stocks": 2}

    @pytest.mark.asyncio
    async def test_handle_with_empty_response(self) -> None:
        response_data = {
            "data": [],
            "status": "ok"
        }

        mock_response = Mock()
        mock_response.json.return_value = response_data
        self.requests_http_client_mock.get.return_value = mock_response
        self.stock_json_schema_validator_mock.validate.return_value = None
        self.stock_repository_mock.save_many.return_value = 0
        result = await self.command_handler.handle()
        assert result == {"stocks_from_api": 0, "saved_stocks": 0}

    @pytest.mark.asyncio
    async def test_handle_with_invalid_response(self) -> None:
        response_data = {
            "data": [],
            "status": "error"
        }

        mock_response = Mock()
        mock_response.json.return_value = response_data
        self.requests_http_client_mock.get.return_value = mock_response
        self.stock_json_schema_validator_mock.validate.return_value = None
        self.stock_repository_mock.save_many.return_value = 0
        result = await self.command_handler.handle()
        assert result == {"stocks_from_api": 0, "saved_stocks": 0}

    @pytest.mark.asyncio
    async def test_handle_with_invalid_json_schema(self) -> None:
        response_data = {
            "content": [],
            "status": "ok"
        }

        mock_response = Mock()
        mock_response.json.return_value = response_data
        self.requests_http_client_mock.get.return_value = mock_response
        self.stock_json_schema_validator_mock.validate.side_effect = jsonschema.exceptions.\
            ValidationError("The json schema is not valid")

        with pytest.raises(jsonschema.exceptions.ValidationError) as exception_info:
            await self.command_handler.handle()
            assert exception_info == "The json schema is not valid"
