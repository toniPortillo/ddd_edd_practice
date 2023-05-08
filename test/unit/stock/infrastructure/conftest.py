import pytest
from sqlalchemy.orm import Session, Query
from unittest.mock import Mock

query_mock = Mock(spec=Query)
session_mock = Mock(spec=Session)
session_mock.query.return_value = query_mock

class DbInstanceMock:
    def __init__(self):
        self.session = session_mock
    
    def __enter__(self):
        return session_mock

    def __exit__(self, *args):
        pass

@pytest.fixture(scope="module")
def db_instance_session():
    fake_query_result = [
        {
            "id": "123e4567-e89b-12d3-a456-426655440000",
            "symbol": "AAPL",
            "name": "Apple Inc.",
            "currency": "USD",
            "exchange": "NASDAQ",
            "mic_code": "XNAS",
            "country": "US",
            "type": "equity",
        },
        {
            "id": "223e4567-e89b-12d3-a456-426655440000",
            "symbol": "GOOG",
            "name": "Alphabet Inc.",
            "currency": "USD",
            "exchange": "NASDAQ",
            "mic_code": "XNAS",
            "country": "US",
            "type": "equity",
        },
    ]
    mock_stocks_mappers_result = []
    for fake_stock in fake_query_result:
        stock_mapper_mock = Mock()
        stock_mapper_mock.id = fake_stock["id"]
        stock_mapper_mock.symbol = fake_stock["symbol"]
        stock_mapper_mock.name = fake_stock["name"]
        stock_mapper_mock.currency = fake_stock["currency"]
        stock_mapper_mock.exchange = fake_stock["exchange"]
        stock_mapper_mock.mic_code = fake_stock["mic_code"]
        stock_mapper_mock.country = fake_stock["country"]
        stock_mapper_mock.type = fake_stock["type"]
        mock_stocks_mappers_result.append(
            stock_mapper_mock
        )

    query_mock.all.return_value = mock_stocks_mappers_result
    db_instance_session = DbInstanceMock
    return db_instance_session
