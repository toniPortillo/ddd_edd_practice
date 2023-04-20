import pytest
from fastapi.testclient import TestClient

from app.ddd_edd_practice_app import app
from test.integration.test_container_subscriber import test_container_subscriber

client = TestClient(app)

@pytest.fixture(scope="session")
def test_app():
    yield app

@pytest.fixture(scope="session")
def test_client():

    yield client
