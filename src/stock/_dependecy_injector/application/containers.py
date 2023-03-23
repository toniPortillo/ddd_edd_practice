from dependency_injector import containers, providers

from src.stock.application.create_stock_command_handler import CreateStockCommandHandler


class CreateStockContainer(containers.DeclarativeContainer):
    stock_repository = providers.Dependency()
    stock_creator = providers.Dependency()

    create_stock_command_handler = providers.Singleton(
        CreateStockCommandHandler,
        stock_repository,
        stock_creator,
    )
