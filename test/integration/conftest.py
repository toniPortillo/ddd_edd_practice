import pytest
from fastapi.testclient import TestClient

from app.ddd_edd_practice_app import app


@pytest.fixture(scope="session")
def test_client():
    client = TestClient(app)
    yield client
