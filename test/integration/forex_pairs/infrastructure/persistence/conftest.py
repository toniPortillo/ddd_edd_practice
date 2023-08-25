import pytest

from src.forex_pairs.infrastructure.persistence.sqlalchemy_forex_pairs_repository import (
    SqlalchemyForexPairsRepository,
)


@pytest.fixture(scope="module")
def sqlalchemy_forex_pairs_repository(database_instance):
    sqlalchemy_forex_pairs_repository = SqlalchemyForexPairsRepository(
        db_instance=database_instance.session,
    )
    yield sqlalchemy_forex_pairs_repository
