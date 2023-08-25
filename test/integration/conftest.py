import os
from typing import Any, Dict, Final, List
import pytest

from fastapi import FastAPI

from fastapi.testclient import TestClient
from dependency_injector import providers
from sqlalchemy.orm import close_all_sessions

from app.config.api.api_v1.api import api_router

from test.integration.config.database_container import DatabaseContainer
from app.config.container_subscriber import container_subscriber
from app.config.configure_database import configure_database


API_V: Final[str] = f"{os.getenv('SUB_PATH', '')}/api/v1"
tags_metadata: List[Dict[str, Any]] = [
    {
        "name": "Port and adapters, FastApi project schema",
        "description": "How to expose endpoints",
    }
]

@pytest.fixture(scope="session", autouse=True)
def containers():
    database_container = providers.Container(
        DatabaseContainer,
    )
    container_subscriber[0] = database_container

    yield container_subscriber

@pytest.fixture(scope="session", autouse=True)
def database_instance(containers):
    database_instance = containers[0].db()
    database_configured = configure_database(database_instance)

    yield database_configured

@pytest.fixture(scope="session", autouse=True)
def create_isolated_db(database_instance):
    database_instance.create_database()
    yield
    close_all_sessions()
    database_instance.drop_database()

@pytest.fixture(scope="session", autouse=True)
def fastapi_app(containers):
    app = FastAPI(
        title = "App for integration testing",
        openapi_url = f"{API_V}/openapi.json",
        openapi_tags = tags_metadata,
    )
    app.container = containers
    app.include_router(api_router, prefix="/api/v1")

    yield app

@pytest.fixture(scope="session")
def test_client(fastapi_app):

    client = TestClient(fastapi_app)
    yield client

@pytest.fixture(scope="class", autouse=True)
def test_class_utils(request, fastapi_app, test_client, database_instance):
    request.cls.fastapi_app = fastapi_app
    request.cls.test_client = test_client
    request.cls.database_instance = database_instance
