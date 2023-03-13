import os
from typing import Any, Dict, Final, List

from fastapi import FastAPI

from app.config.singleton_aiohttp import SingletonAiohttp
from app.config.api.api_v1.api import api_router
from app.config.containers import ApplicationContainer


API_V: Final[str] = f"{os.getenv('SUB_PATH', '')}/api/v1"
tags_metadata: List[Dict[str, Any]] = [
    {
        "name": "Port and adapters, FastApi project schema",
        "description": "How to expose endpoints",
    }
]


async def on_start_up() -> None:
    SingletonAiohttp.get_aiohttp_client()
    application = ApplicationContainer()
    application.wire(modules=[__name__])

async def on_shutdown() -> None:
    await SingletonAiohttp.close_aiohttp_client()


app = FastAPI(
    title="Port and adapters, FastApi project schema",
    openapi_url=f"{API_V}/openapi.json",
    openapi_tags=tags_metadata,
    on_startup=[on_start_up],
    on_shutdown=[on_shutdown],
)

app.include_router(api_router, prefix=API_V)
