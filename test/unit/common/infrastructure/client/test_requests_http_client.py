from requests import Response

import pytest

from src.common.infrastructure.client.requests_http_client import RequestsHttpClient


@pytest.mark.asyncio
class TestRequestsHttpClient:
    async def test_get(self, response_mock, requests_session_mock):\
        #Arrange
        response_mock.status_code = 200
        response_mock.json.return_value = {"data": []}
        fake_url: str = 'https://fake-url.com'
        
        #Act
        requests_http_client = RequestsHttpClient(
            url=fake_url,
            session_requests=requests_session_mock,
        )

        response: Response = await requests_http_client.get('/stocks')

        #Assert
        assert response.status_code == 200
        assert response.json() == {"data": []}
        requests_session_mock.session_requests.assert_called_once_with(
            url=f'{fake_url}/stocks',
            method='get',
            headers={},
            timeout=None,
            retry_policy=None,
        )

    async def test_get_with_access_token_value(self, response_mock, requests_session_mock):
        #Arrange
        response_mock.status_code = 200
        response_mock.json.return_value = {"data": []}
        fake_url: str = 'https://fake-url.com'
        requests_http_client = RequestsHttpClient(
            url=fake_url,
            session_requests=requests_session_mock,
        )
        fake_access_token_value: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\
        eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.\
        SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

        #Act
        response: Response = await requests_http_client.get(
            path='/stocks',
            access_token_value=fake_access_token_value,
        )

        #Assert
        assert response.status_code == 200
        assert response.json() == {"data": []}
        requests_session_mock.session_requests.assert_called_once_with(
            url=f'{fake_url}/stocks',
            method='get',
            headers={"Authorization": f"Bearer {fake_access_token_value}"},
            timeout=None,
            retry_policy=None,
        )

    async def test_get_with_language(self, response_mock, requests_session_mock):
        #Arrange
        response_mock.status_code = 200
        response_mock.json.return_value = {"data": []}
        fake_url: str = 'https://fake-url.com'

        #Act
        requests_http_client = RequestsHttpClient(
            url=fake_url,
            session_requests=requests_session_mock,
        )
        response: Response = await requests_http_client.get(
            path='/stocks',
            language='es',
        )

        #Assert
        assert response.status_code == 200
        assert response.json() == {"data": []}
        requests_session_mock.session_requests.assert_called_once_with(
            url=f'{fake_url}/stocks',
            method='get',
            headers={"Accept-Language": "es"},
            timeout=None,
            retry_policy=None,
        )
