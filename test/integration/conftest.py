import pytest
from fastapi.testclient import TestClient

from app.ddd_edd_practice_test_app import test_app


@pytest.fixture(scope="session")
def test_client():
    client = TestClient(test_app)
    yield client
