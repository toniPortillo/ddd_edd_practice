import pytest
from fastapi.testclient import TestClient
from dependency_injector import providers
from sqlalchemy.orm import close_all_sessions, clear_mappers, registry

from app.config.mapper_subscriber import mapper_subscriber
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
    database_instance = database_container.db()
    
    clear_mappers()
    mapper_registry = registry()
    
    mappers = mapper_subscriber(database_instance)
    for mapper in mappers:
        mapper_registry.map_imperatively(
            mapper.entity(), 
            mapper.table()
        )

    yield database_instance


@pytest.fixture(scope="session")
def test_client(fastapi_app):
    client = TestClient(fastapi_app)
    yield client

@pytest.fixture(scope="class", autouse=True)
def test_class_utils(request, fastapi_app, test_client, database_instance):
    request.cls.fastapi_app = fastapi_app
    request.cls.test_client = test_client
    request.cls.database_instance = database_instance

@pytest.fixture(scope="session", autouse=True)
def create_isolated_db(database_instance):
    database_instance.create_database()
    yield
    close_all_sessions()
    database_instance.drop_database()
