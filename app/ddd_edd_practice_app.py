import os
from typing import Any, Dict, Final, List

from fastapi import FastAPI
from dependency_injector import containers

from app.config.api.api_v1.api import api_router
from app.config.container_subscriber import container_subscriber
from app.config.configure_database import configure_database


API_V: Final[str] = f"{os.getenv('SUB_PATH', '')}/api/v1"
tags_metadata: List[Dict[str, Any]] = [
    {
        "name": "Port and adapters, FastApi project schema",
        "description": "How to expose endpoints",
    }
]


async def on_start_up() -> None:
    configure_database()

async def on_shutdown() -> None:
    containers.unwire()


def create_app() -> FastAPI:
    app = FastAPI(
        title = "Port and adapters, FastApi project schema",
        openapi_url = f"{API_V}/openapi.json",
        openapi_tags = tags_metadata,
        on_startup = [on_start_up],
        on_shutdown = [on_shutdown],

    )
    app.container = container_subscriber
    app.include_router(api_router, prefix="/api/v1")
    return app

app = create_app()
