from dependency_injector import providers

from test.integration.config.database_container import DatabaseContainer

database_container = providers.Container(
    DatabaseContainer,
)

test_container_subscriber = [
    database_container,
]
