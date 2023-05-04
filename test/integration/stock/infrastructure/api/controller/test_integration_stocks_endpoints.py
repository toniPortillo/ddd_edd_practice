import pytest
from unittest.mock import AsyncMock, Mock

from common.infrastructure.client.requests_http_client import RequestsHttpClient
from src.stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from stock.application.create_stock_command_handler import CreateStockCommandHandler


@pytest.mark.asyncio
class TestIntegrationStocksEndpoints:
    async def test_get_stocks(self) -> None:
        create_stock_command_handler_mock = AsyncMock(CreateStockCommandHandler)
        create_stock_command_handler_mock.handle.return_value = {"stocks_from_api": 2, "saved_stocks": 2}
        with self.fastapi_app.container[1].create_stock_command_handler.override(create_stock_command_handler_mock):
            response = self.test_client.post("/api/v1/stocks")

        assert response.status_code == 201

    async def test_get_stocks_with_requests_http_client_mock(self) -> None:
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
                }
            ],
            "status": "ok"
        }

        mock_response: Mock = Mock()
        mock_response.json.return_value = response_data
        requests_http_client_mock = AsyncMock(RequestsHttpClient)
        requests_http_client_mock.get.return_value = mock_response

        with self.fastapi_app.container[1].requests_http_client.override(requests_http_client_mock):
            response = self.test_client.post("/api/v1/stocks")

        assert response.status_code == 201
        assert response.json() == {"stocks_from_api": 2, "saved_stocks": 2}
