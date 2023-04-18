import jsonschema


class StockJsonSchemaValidator:
    stock_json_schema = {
        "type": "object",
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                        "name": {"type": "string"},
                        "currency": {"type": "string"},
                        "exchange": {"type": "string"},
                        "mic_code": {"type": "string"},
                        "country": {"type": "string"},
                        "type": {"type": "string"},
                    },
                },
                "required": ["symbol", "name", "currency", "exchange", "mic_code", "country", "type"],
            },
            "status": {"type": "string"},
        },
        "required": ["data", "status"],
    }

    async def validate(self, stock_json: dict) -> None:
        try:
            jsonschema.validate(instance=stock_json, schema=self.stock_json_schema)
        except jsonschema.exceptions.ValidationError:
            raise jsonschema.exceptions.ValidationError("The json schema is not valid")
