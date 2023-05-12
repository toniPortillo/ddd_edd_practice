from src.forex_pairs.domain.forex_pairs import ForexPairs
from src.forex_pairs.domain.forex_pairs_creator import ForexPairsCreator


class ForexPairsMother:
    @classmethod
    async def forex_pairs_1(cls) -> ForexPairs:
        return await ForexPairsCreator.create(
            symbol="EUR/USD",
            currency_group="Major",
            currency_base="Euro",
            currency_quote="US Dollar",
        )

    @classmethod
    async def forex_pairs_2(cls) -> ForexPairs:
        return await ForexPairsCreator.create(
            symbol="XAU/USD",
            currency_group="Exotic",
            currency_base="Gold Spot",
            currency_quote="US Dollar",
        )
