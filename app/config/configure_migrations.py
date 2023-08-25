from alembic import command
from alembic.config import Config


def configure_migrations() -> None:
    alembic_cfg = Config("/srv/app/migrations/alembic.ini")
    command.stamp(alembic_cfg, "head")
