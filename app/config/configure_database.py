from typing import List
from sqlalchemy.orm import clear_mappers, registry

from app.config.container_subscriber import container_subscriber
#from app.config.mapper_subscriber import mapper_subscriber
#from src.forex_pairs.domain.forex_pairs import ForexPairs
#from src.forex_pairs.infrastructure.persistence.forex_pairs_mapper import ForexPairsMapper

def configure_database() -> None:
    db = container_subscriber[0].db()
    db.create_database()

    clear_mappers()
    mapper_registry = registry()

    #mapper_registry.map_imperatively(ForexPairs, 'forex_pairs')
