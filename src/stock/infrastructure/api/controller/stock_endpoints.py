from typing import Dict, Union

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from dependency_injector.wiring import Provide, inject

from app.config.error_handlers.application_exception import (
    ApplicationException,
)

from src.stock._dependency_injector.infrastructure.api.controller.stock_endpoints import StockEndpointsContainer
from src.stock.application.create_stock_response_dto import CreateStockResponseDto
from src.stock.application.create_stock_command_handler import CreateStockCommandHandler

router = APIRouter()


@router.post(
    "",
    status_code=201,
    response_model=CreateStockResponseDto,
    summary="Endpoint to add a stock to the system",
)
@inject
async def create_stock(
    create_stock_command_handler: CreateStockCommandHandler = Depends(
        Provide[StockEndpointsContainer.create_stock_command_handler]
    ),
) -> Union[CreateStockResponseDto, JSONResponse]:
    try:
        result: Dict = await create_stock_command_handler.handle()
        return CreateStockResponseDto(
            stocks_from_api=result["stocks_from_api"],
            saved_stocks=result["saved_stocks"],
        )
    except ApplicationException:
        return JSONResponse(status_code=500, content={"message": "Error creating stock"})
