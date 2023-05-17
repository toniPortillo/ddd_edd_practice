from dependency_injector import containers, providers

from src.stock.infrastructure.persistence.stock_mapper import StockMapper


class StockMapperContainer(containers.DeclarativeContainer):
    db_instance = providers.Dependency()

    stock_mapper = providers.Factory(
        StockMapper,
        db_instance=db_instance,
    )
