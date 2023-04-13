from dependency_injector import containers, providers

from src.stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from src.stock.domain.stock_creator import StockCreator
from src.stock.application.create_stock_command_handler import CreateStockCommandHandler

from app.config.database import Database


class ApplicationContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.stock.infrastructure.api.controller.stock_endpoints"])
    config = providers.Configuration(yaml_files=['config.yml'])

    db = providers.Singleton(Database, db_url=config.database.dsn)
    
    stock_repository = providers.Factory(
        SqlalchemyStockRepository,
        db_instance=db.provided.session,
    )

    stock_creator = providers.Factory(
        StockCreator,
    )

    create_stock_command_handler = providers.Factory(
        CreateStockCommandHandler,
        stock_repository=stock_repository,
        stock_creator=stock_creator,
    )
