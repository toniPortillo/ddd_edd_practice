from typing import Any, Union

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.config.api.api_v1.error.standar_errors import NOT_FOUND_STATUS_CODE
from app.config.error_handlers.application_exception import (
    ApplicationException,
)

router = APIRouter()


@router.get("/", summary="Show a hello world!", status_code=200, response_model=None)
async def hello_world_endpoint() -> Union[str, JSONResponse]:
    try:
        return "Hello world!"
    except ApplicationException:
        return JSONResponse(status_code=NOT_FOUND_STATUS_CODE, content={"message": ""})
