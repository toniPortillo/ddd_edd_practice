from typing import List
from sqlalchemy.orm import clear_mappers, registry

from dependency_injector import providers

from app.config.container_subscriber import container_subscriber
from src.forex_pairs._dependency_injector.infrastructure.persistence.forex_pairs_mapper_container import ForexPairsMapperContainer
from src.forex_pairs.domain.forex_pairs import ForexPairs
from src.forex_pairs.infrastructure.persistence.forex_pairs_mapper import ForexPairsMapper

def configure_database() -> None:
    db = container_subscriber[0].db()
    db.create_database()

    clear_mappers()
    mapper_registry = registry()

    forex_pairs_mapper_container = providers.Container(
        ForexPairsMapperContainer,
        db_instance=db,
    )

    mapper_registry.map_imperatively(
        forex_pairs_mapper_container.forex_pairs_mapper().entity(), 
        forex_pairs_mapper_container.forex_pairs_mapper().table()
)
