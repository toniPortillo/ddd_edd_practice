from dependency_injector import containers, providers

from src.stock.domain.stock_creator import StockCreator


class StockCreatorContainer(containers.DeclarativeContainer):
    stock_creator = providers.Singleton(
        StockCreator,
    )
