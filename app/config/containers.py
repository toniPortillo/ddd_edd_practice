from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.stock._dependecy_injector.infrastructure.containers import StockContainer


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=['config.ini'])

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

    stock_container = providers.Container(
        StockContainer,
        db_instance=session,
    )
