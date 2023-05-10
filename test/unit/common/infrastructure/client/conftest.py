from unittest.mock import Mock
from requests import Response, Session
from requests.adapters import HTTPAdapter, Retry

import pytest

from src.common.infrastructure.client.requests_session import RequestsSession


@pytest.fixture(scope='function')
def http_adapter_mock():
    http_adapter_mock = Mock(spec=HTTPAdapter)
    yield http_adapter_mock

@pytest.fixture(scope='function')
def retry_mock():
    retry_mock = Mock(spec=Retry)
    yield retry_mock

@pytest.fixture(scope='function')
def response_mock():
    response_mock = Mock(spec=Response)
    yield response_mock

@pytest.fixture(scope='function')
def requests_session_mock(response_mock):
    requests_session_mock = Mock(spec=RequestsSession)
    requests_session_mock.session_requests.return_value = response_mock
    yield requests_session_mock

@pytest.fixture(scope='function')
def session_mock():
    session_mock = Mock(spec=Session)
    yield session_mock
