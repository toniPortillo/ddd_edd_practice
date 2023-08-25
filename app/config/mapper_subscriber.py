from typing import List

from dependency_injector import providers
from sqlalchemy.orm import clear_mappers, registry, mapper

from app.config.database import Database
from src.common.infrastructure.persistence.mapper import Mapper
from src.forex_pairs._dependency_injector.infrastructure.persistence.forex_pairs_mapper_container import ForexPairsMapperContainer
from src.stock._dependency_injector.infrastructure.persistence.stock_mapper_container import StockMapperContainer

def mapper_subscriber(db_instance: Database) -> List[Mapper]:
    
    forex_pairs_mapper_container = providers.Container(
        ForexPairsMapperContainer,
        db_instance=db_instance,
    )
    print(forex_pairs_mapper_container.forex_pairs_mapper())
    stock_mapper_container = providers.Container(
        StockMapperContainer,
        db_instance=db_instance,
    )
    print(stock_mapper_container.stock_mapper())

    mappers: List[Mapper] = [
        stock_mapper_container.stock_mapper(),
        forex_pairs_mapper_container.forex_pairs_mapper(),
    ]

    for entity_mapper in mappers:
        mapper(
            entity_mapper.entity(),
            entity_mapper.table(),
        )

    # list(map(lambda mapper: mapper_registry.map_imperatively(
    #     mapper.entity(),
    #     mapper.table(),
    # ), mappers))
