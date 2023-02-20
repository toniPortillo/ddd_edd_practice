import asyncio
from socket import AF_INET
from typing import Optional

from fastapi import APIRouter

import aiohttp

SIZE_POOL_AIOHTTP = 100


class SingletonAiohttp:
    semaphore: Optional[asyncio.Semaphore] = None
    aiohttp_client: Optional[aiohttp.ClientSession] = None

    @classmethod
    def get_aiohttp_client(cls) -> aiohttp.ClientSession:
        if cls.aiohttp_client is None:
            timeout = aiohttp.Clien