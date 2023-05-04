from typing import List
from sqlalchemy.orm import clear_mappers, registry

from app.config.container_subscriber import container_subscriber


def configure_database() -> None:
    db = container_subscriber[0].db()
    db.create_database()
