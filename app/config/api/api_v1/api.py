from fastapi import APIRouter

from src.hello_world.infrastructure.api.controller import hello_endpoints
from src.stock.infrastructure.api.controller import stock_endpoints


api_router = APIRouter()
api_router.include_router(
    hello_endpoints.router, prefix="/helloworlds", tags=["HelloWorld"],
)
api_router.include_router(
    stock_endpoints.router, prefix="/stocks", tags=["Stocks"],
)
