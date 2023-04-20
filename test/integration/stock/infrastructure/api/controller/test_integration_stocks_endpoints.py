

class TestIntegrationStocksEndpoints:
    def test_get_stocks(self, test_client):
        response = test_client.post("http://localhost:5000/api/v1/stocks")

        assert response.status_code == 201
