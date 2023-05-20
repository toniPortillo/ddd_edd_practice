from uuid import uuid4

from forex_pairs.domain.forex_pairs import ForexPairs


class ForexPairsCreator:
    @classmethod
    async def create(
        self,
        symbol: str,
        currency_group: str,
        currency_base: str,
        currency_quote: str,
    ) -> ForexPairs:
        return ForexPairs(
            id=uuid4(),
            symbol=symbol,
            currency_group=currency_group,
            currency_base=currency_base,
            currency_quote=currency_quote,
        )
