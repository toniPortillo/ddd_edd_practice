from typing import List
import pytest

from src.forex_pairs.infrastructure.persistence.sqlalchemy_forex_pairs_repository import (
    SqlalchemyForexPairsRepository,
)
from src.forex_pairs.domain.forex_pairs import ForexPairs
from test.mothers.forex_pairs.forex_pairs_mother import ForexPairsMother


@pytest.fixture(scope="module")
def sqlalchemy_forex_pairs_repository(database_instance):
    sqlalchemy_forex_pairs_repository = SqlalchemyForexPairsRepository(
        db_instance=database_instance.session,
    )
    yield sqlalchemy_forex_pairs_repository
