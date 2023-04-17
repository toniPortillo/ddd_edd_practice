from dependency_injector import containers, providers

from app.config.containers import ApplicationContainer
from src.stock._dependency_injector.infrastructure.api.controller.stock_endpoints import StockEndpointsContainer


application_container = ApplicationContainer()
stock_endpoints_container = providers.Container(
    StockEndpointsContainer,
    db_session=application_container.db.provided.session,
)
container_subscriber = [
    application_container,
    stock_endpoints_container,
]