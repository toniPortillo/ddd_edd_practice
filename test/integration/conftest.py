import pytest
from fastapi.testclient import TestClient
from dependency_injector import providers
from sqlalchemy.orm import close_all_sessions

from app.ddd_edd_practice_app import create_app
from test.integration.config.database_container import DatabaseContainer


@pytest.fixture(scope="session", autouse=True)
def fastapi_app():
    app = create_app()
    yield app

@pytest.fixture(scope="session", autouse=True)
def database_instance(fastapi_app):
    database_container = providers.Container(
        DatabaseContainer,
    )
    fastapi_app.container[0].override(database_container)
    yield database_container.db()


@pytest.fixture(scope="session")
def test_client(fastapi_app):
    client = TestClient(fastapi_app)
    yield client

@pytest.fixture(scope="class", autouse=True)
def test_class_utils(request, fastapi_app, test_client):
    request.cls.fastapi_app = fastapi_app
    request.cls.test_client = test_client

@pytest.fixture(scope="session", autouse=True)
def create_isolated_db(database_instance):
    database_instance.create_database()
    yield
    close_all_sessions()
    database_instance.drop_database()
