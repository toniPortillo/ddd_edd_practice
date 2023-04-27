import pytest
from fastapi.testclient import TestClient
from dependency_injector import providers

from app.ddd_edd_practice_app import app
from test.integration.config.database_container import DatabaseContainer


@pytest.fixture(scope="session", autouse=True)
def test_db_configuration():
    database_container = providers.Container(
        DatabaseContainer,
    )
    app.container[0].override(database_container)

@pytest.fixture(scope="session")
def test_client():
    client = TestClient(app)
    yield client
