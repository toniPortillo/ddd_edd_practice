from typing import List
from dependency_injector import providers

from test.integration.config.database_container import DatabaseContainer
from stock._dependency_injector.infrastructure.api.controller.stock_endpoints import StockEndpointsContainer


database_container = providers.Container(
    DatabaseContainer,
)
stock_endpoints_container = providers.Container(
    StockEndpointsContainer,
    db_session=database_container.db.provided.session,
)

test_container_subscriber: List = [
    database_container,
    stock_endpoints_container,
]
