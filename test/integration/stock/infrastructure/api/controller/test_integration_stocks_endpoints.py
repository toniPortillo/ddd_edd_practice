

class TestIntegrationStocksEndpoints:
    def test_get_stocks(self, test_client):
        response = test_client.post("/api/v1/stocks")

        assert response.status_code == 201
