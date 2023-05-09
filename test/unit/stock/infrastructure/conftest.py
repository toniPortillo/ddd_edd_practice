import pytest
from sqlalchemy.orm import Session, Query
from unittest.mock import Mock

class DbInstanceMock:
    session_mock = Mock(spec=Session)
    
    def __enter__(self):
        return self.session_mock

    def __exit__(self, *args):
        pass

@pytest.fixture(scope="function")
def query_mock():
    yield Mock(spec=Query)

@pytest.fixture(scope="function")
def db_instance_session():
    yield DbInstanceMock
