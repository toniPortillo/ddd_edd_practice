from dependency_injector import containers, providers

from src.stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from src.stock.domain.stock_creator import StockCreator
from src.stock.application.create_stock_command_handler import CreateStockCommandHandler
from src.common.infrastructure.client.requests_session import RequestsSession
from src.common._dependency_injector.infrastructure.requests_http_client import RequestsHttpClientContainer

from app.config.database import Database


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['config.yml'])

    db = providers.Singleton(Database, db_url=config.database.dsn)
