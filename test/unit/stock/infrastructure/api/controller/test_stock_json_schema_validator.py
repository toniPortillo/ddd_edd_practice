import pytest
import jsonschema

from src.stock.infrastructure.api.controller.stock_json_schema_validator import StockJsonSchemaValidator


@pytest.mark.asyncio
class TestStockJsonSchemaValidator:
    async def test_validate(self, mocker):
        # Arrange
        stock_json_fake = {
            "data": [
                {
                    "symbol": "AAPL",
                    "name": "Apple Inc.",
                    "currency": "USD",
                    "exchange": "NASDAQ",
                    "mic_code": "XNAS",
                    "country": "United States",
                    "type": "Common Stock",
                },
                {
                    "symbol": "MSFT",
                    "name": "Microsoft Corporation",
                    "currency": "USD",
                    "exchange": "NASDAQ",
                    "mic_code": "XNAS",
                    "country": "United States",
                    "type": "Common Stock",
                },
            ],
            "status": "ok"
        }

        # Act
        stock_json_schema_validator = StockJsonSchemaValidator()

        # Assert
        with mocker.patch('src.stock.infrastructure.api.controller.stock_json_schema_validator.jsonschema.validate'):
            response = await stock_json_schema_validator.validate(stock_json_fake)
            jsonschema.validate.assert_called_once_with(instance=stock_json_fake, schema=stock_json_schema_validator.stock_json_schema)
            assert response is None

    async def test_validate_validation_exception(self):
        # Arrange
        stock_json_fake = {
            "error": [
                {}
            ],
            "status_code": "error"
        }

        # Act
        stock_json_schema_validator = StockJsonSchemaValidator()

        # Assert
        with pytest.raises(jsonschema.exceptions.ValidationError):
            await stock_json_schema_validator.validate(stock_json_fake)
