from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository
from src.stock.domain.stock_creator import StockCreator
from src.stock.application.create_stock_command_handler import CreateStockCommandHandler


class ApplicationContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.stock.infrastructure.api.controller.stock_endpoints"])
    config = providers.Configuration(yaml_files=['config.yml'])
    print(config.database.dsn)
    engine = providers.Singleton(
        create_engine,
        config.database.dsn,
    )

    session = providers.Singleton(
        sessionmaker,
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    Base = providers.Singleton(
        declarative_base
    )

    stock_repository = providers.Factory(
        SqlalchemyStockRepository,
        db_instance=session,
    )

    stock_creator = providers.Factory(
        StockCreator,
    )

    create_stock_command_handler = providers.Factory(
        CreateStockCommandHandler,
        stock_repository=stock_repository,
        stock_creator=stock_creator,
    )
