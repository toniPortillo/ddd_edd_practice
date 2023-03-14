from typing import Union

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.config.error_handlers.application_exception import (
    ApplicationException,
)
from src.stock.application.create_stock_dto import CreateStockDto
from src.stock.application.create_stock_response_dto import CreateStockResponseDto

router = APIRouter()


@router.post(
    "",
    status_code=201,
    response_model=CreateStockResponseDto,
    summary="Endpoint to add a stock to the system",
)
async def create_stock(
    create_stock_dto: CreateStockDto,
) -> Union[CreateStockResponseDto, JSONResponse]:
    try:
        return CreateStockResponseDto(id="123")
    except ApplicationException:
        return JSONResponse(status_code=500, content={"message": "Error creating stock"})
