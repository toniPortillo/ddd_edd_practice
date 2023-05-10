from unittest.mock import Mock
from requests import Response, Session
from requests.adapters import HTTPAdapter, Retry

import pytest

from src.common.infrastructure.client.requests_session import RequestsSession


@pytest.fixture(scope='function')
def http_adapter_mock(mocker):
    http_adapter_mock = Mock(spec=HTTPAdapter)
    mocker.patch('src.common.infrastructure.client.requests_session.HTTPAdapter', return_value=http_adapter_mock)
    yield http_adapter_mock

@pytest.fixture(scope='function')
def retry_mock(mocker):
    retry_mock = Mock(spec=Retry)
    mocker.patch('src.common.infrastructure.client.requests_session.Retry', return_value=retry_mock)
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
def session_mock(mocker):
    session_mock = Mock(spec=Session)
    mocker.patch('src.common.infrastructure.client.requests_session.Session', return_value=session_mock)
    yield session_mock
