from dependency_injector import containers, providers
from src.stock.infrastructure.sqlalchemy_stock_repository import SqlalchemyStockRepository


class SqlalchemyStockRepositoryContainer(containers.DeclarativeContainer):
    db_instance = providers.Dependency()

    sqlalchemy_stock_repository = providers.Singleton(
        SqlalchemyStockRepository,
        db_instance,
    )
