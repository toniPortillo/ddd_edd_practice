import pytest

from src.common.infrastructure.client.requests_session import RequestsSession


@pytest.mark.asyncio
class TestRequestsSession:
    def test_session_requests(self, mocker, retry_mock, http_adapter_mock, response_mock, session_mock):
        # Arrange
        response_mock.status_code = 200
        response_mock.json.return_value = {"data": []}
        session_mock.mount.return_value = None
        session_mock.request.return_value = response_mock

        fake_url: str = "https://fake-url.com/stocks"

        # Act
        response = RequestsSession.session_requests(
            url=fake_url,
            method="get",
            headers={},
            timeout=None,
            retry_policy=None,
        )

        # Assert
        assert response.status_code == 200
        assert response.json() == {"data": []}
        assert session_mock.mount.called_once_with(fake_url, http_adapter_mock)
        assert session_mock.request.called_once_with(fake_url, method="get", headers={}, timeout=None)

    def test_session_requests_data_or_json_not_none(self, mocker, retry_mock, http_adapter_mock, session_mock, response_mock):
        # Arrange
        response_mock.status_code = 200
        response_mock.json.return_value = {"data": []}
        session_mock.mount.return_value = None
        session_mock.request.return_value = response_mock

        fake_url: str = "https://fake-url.com/stocks"

        # Act
        kwargs = {"data": "fake_data", "json": "fake_json"}
        response = RequestsSession.session_requests(
            url=fake_url,
            method="get",
            headers={},
            timeout=None,
            retry_policy=None,
            **kwargs,
        )

        # Assert
        assert response_mock.status_code == 200
        assert response_mock.json() == {"data": []}
        assert session_mock.mount.called_once_with(fake_url, http_adapter_mock)
        assert session_mock.request.called_once_with(fake_url, method="get", headers={}, timeout=None, data="fake_data", json="fake_json")
