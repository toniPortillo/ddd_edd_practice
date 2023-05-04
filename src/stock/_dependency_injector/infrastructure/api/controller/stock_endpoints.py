from dependency_injector import containers, providers

from src.common._dependency_injector.infrastructure.requests_session import RequestsSessionContainer
from src.stock._dependency_injector.infrastructure.sqlalchemy_stock_repository_container import (
    SqlalchemyStockRepositoryContainer,
)
from src.common.infrastructure.client.requests_http_client import RequestsHttpClient
from src.stock._dependency_injector.domain.stock_creator_container import StockCreatorContainer
from stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from src.stock.application.create_stock_command_handler import CreateStockCommandHandler
from src.stock.infrastructure.api.controller.stock_json_schema_validator import StockJsonSchemaValidator


class StockEndpointsContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.stock.infrastructure.api.controller.stock_endpoints"])
    config = providers.Configuration(yaml_files=["config.yml"])

    db_session = providers.Dependency()
    """
    sqlalchemy_stock_repository_container = providers.Container(
        SqlalchemyStockRepositoryContainer,
        db_instance=db_session,
    )
    """
    sqlalchemy_stock_repository = providers.Singleton(
        SqlalchemyStockRepository,
        db_instance=db_session,
    )

    stock_creator_container = providers.Container(
        StockCreatorContainer,
    )

    session_requests_container = providers.Container(
        RequestsSessionContainer,
    )

    requests_http_client = providers.Factory(
        RequestsHttpClient,
        session_requests=session_requests_container.requests_session,
        url=config.api.url,
    )

    stock_json_schema_validator = providers.Factory(
        StockJsonSchemaValidator,
    )

    create_stock_command_handler = providers.Factory(
        CreateStockCommandHandler,
        stock_repository=sqlalchemy_stock_repository,
        stock_creator=stock_creator_container.stock_creator,
        requests_http_client=requests_http_client,
        stock_json_schema_validator=stock_json_schema_validator,
    )
