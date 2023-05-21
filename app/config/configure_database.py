from typing import List

from alembic import command
from alembic.config import Config

from app.config.container_subscriber import container_subscriber
from app.config.mapper_subscriber import mapper_subscriber


def configure_database() -> None:
    alembic_cfg = Config("/srv/app/migrations/alembic.ini")
    command.stamp(alembic_cfg, "head")

    db = container_subscriber[0].db()

    mapper_subscriber(db)
    db.create_database()
