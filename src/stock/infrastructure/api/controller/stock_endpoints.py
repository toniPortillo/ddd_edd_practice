from typing import Union

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from dependency_injector.wiring import Provide, inject

from app.config.error_handlers.application_exception import (
    ApplicationException,
)
from app.config.containers import ApplicationContainer
from src.stock.application.create_stock_dto import CreateStockDto
from src.stock.application.create_stock_response_dto import CreateStockResponseDto
from src.stock.application.create_stock_command import CreateStockCommand
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
    create_stock_dto: CreateStockDto,
    create_stock_command_handler: CreateStockCommandHandler = Depends(
        Provide[ApplicationContainer.create_stock_command_handler]
    ),
) -> Union[CreateStockResponseDto, JSONResponse]:
    try:
        create_stock_command: CreateStockCommand = CreateStockCommand(
            symbol=create_stock_dto.symbol,
            name=create_stock_dto.name,
            currency=create_stock_dto.currency,
            exchange=create_stock_dto.exchange,
            mic_code=create_stock_dto.mic_code,
            country=create_stock_dto.country,
            type=create_stock_dto.type,
        )
        print(create_stock_command_handler)
        await create_stock_command_handler.handle(create_stock_command)
        return CreateStockResponseDto(
            stock_id=123,
            response="Stock created",
        )
    except ApplicationException:
        return JSONResponse(status_code=500, content={"message": "Error creating stock"})
