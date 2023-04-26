import os
from typing import Any, Final, List, Dict

from fastapi import FastAPI
from dependency_injector import containers

from app.config.api.api_v1.api import api_router
from test.integration.test_container_subscriber import test_container_subscriber


API_V: Final[str] = f"{os.getenv('SUB_PATH', '')}/api/v1"
tags_metadata: List[Dict[str, Any]] = [
    {
        "name": "Port and adapters, FastApi project schema",
        "description": "Application for integration testing",
    }
]

async def on_test_start_up() -> None:
    db = test_container_subscriber[0].db()
    db.create_database()

async def on_test_shutdown() -> None:
    containers.unwire()


def create_test_app() -> FastAPI:
    app = FastAPI(
        title = "Port and adapters, FastApi project schema",
        openapi_url = f"{API_V}/openapi.json",
        openapi_tags = tags_metadata,
        on_startup = [on_test_start_up],
        on_shutdown = [on_test_shutdown],

    )
    app.container = test_container_subscriber
    app.include_router(api_router, prefix="/api/v1")
    return app

test_app = create_test_app()
