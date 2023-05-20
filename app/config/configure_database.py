from typing import List

from alembic import command
from alembic.config import Config
from sqlalchemy.orm import clear_mappers, registry

from app.config.container_subscriber import container_subscriber
from app.config.mapper_subscriber import mapper_subscriber
from common.infrastructure.persistence.mapper import Mapper

def configure_database() -> None:
    alembic_cfg = Config("/srv/app/migrations/alembic.ini")
    command.stamp(alembic_cfg, "head")

    db = container_subscriber[0].db()

    clear_mappers()

    mapper_registry = registry()
    
    mappers: List[Mapper] = mapper_subscriber(db)

    for mapper in mappers:
        mapper_registry.map_imperatively(
            mapper.entity(), 
            mapper.table()
        )

    db.create_database()
