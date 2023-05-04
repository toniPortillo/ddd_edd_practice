import pytest
from unittest.mock import AsyncMock, Mock

from common.infrastructure.client.requests_http_client import RequestsHttpClient


@pytest.mark.asyncio
class TestIntegrationStocksEndpoints:
    async def test_get_stocks(self) -> None:
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
                },
                {...}
            ],
            "status": "ok"
        }

        mock_response: Mock = Mock()
        mock_response.json.response.return_value = response_data
        requests_http_client_mock = AsyncMock(RequestsHttpClient)
        requests_http_client_mock.get.return_value = mock_response

        self.fastapi_app.dependency_overrides[RequestsHttpClient] = requests_http_client_mock

        response = self.test_client.post("/api/v1/stocks")

        assert response.status_code == 201
