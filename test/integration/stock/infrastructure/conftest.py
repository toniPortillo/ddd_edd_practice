import pytest
from dependency_injector import providers

from src.stock._dependency_injector.domain.stock_creator_container import StockCreatorContainer
from src.stock._dependency_injector.infrastructure.sqlalchemy_stock_repository_container import (
    SqlalchemyStockRepositoryContainer,
)

from test.integration.conftest import database_instance


@pytest.fixture(scope="module")
def sqlalchemy_stock_repository(database_instance):
    sqlalchemy_stock_repository_container = providers.Container(
        SqlalchemyStockRepositoryContainer,
        db_instance=database_instance.session,
    )
    
    yield sqlalchemy_stock_repository_container.sqlalchemy_stock_repository()
