from typing import List

import pytest

from forex_pairs.domain.forex_pairs import ForexPairs
from test.mothers.forex_pairs.forex_pairs_mother import ForexPairsMother


@pytest.mark.asyncio
class TestIntegrationSqlalchemyForexPairsRepository:
    async def test_save_many(self, sqlalchemy_forex_pairs_repository):
        forex_pairs_list: List[ForexPairs] = [
            await ForexPairsMother.forex_pairs_1(),
            await ForexPairsMother.forex_pairs_2(),
        ]
        forex_pairs_saved: int = await sqlalchemy_forex_pairs_repository.save_many(forex_pairs_list)
        assert forex_pairs_saved == 2


    async def test_find_all(self, sqlalchemy_forex_pairs_repository):
        forex_pairs_list: List[ForexPairs] = [
            await ForexPairsMother.forex_pairs_1(),
            await ForexPairsMother.forex_pairs_2(),
        ]
        await sqlalchemy_forex_pairs_repository.save_many(
            forex_pairs_list=forex_pairs_list
        )
        forex_pairs_saved: List[ForexPairs] = await sqlalchemy_forex_pairs_repository.find_all()
        
        assert len(forex_pairs_saved) == 2
