from uuid import UUID
from typing import Callable, ContextManager, List, Iterable

from sqlalchemy.orm import Session

from forex_pairs.domain.forex_pairs import ForexPairs
from forex_pairs.infrastructure.persistence.forex_pairs_mapper import ForexPairsMapper
from forex_pairs.domain.forex_pairs_repository import ForexPairsRepository


class SqlalchemyForexPairsRepository(ForexPairsRepository):
    def __init__(self, db_instance: Callable[..., ContextManager[Session]]):
        self.__db_instance = db_instance

    async def save_many(self, forex_pairs_list: List[ForexPairs]) -> int:
        forex_pairs_mapped: List[ForexPairsMapper] = await self.__domain_to_mappers(forex_pairs_list)

        with self.__db_instance() as session:
            session.add_all(forex_pairs_mapped)
            session.commit()
            return len(forex_pairs_mapped)

    async def __mappers_to_domain(self, forex_pairs_mappers: List[ForexPairsMapper]) -> List[ForexPairs]:
        forex_pairs_list: Iterable[ForexPairs] = map(
            lambda forex_pair_mapper: ForexPairs(
                forex_pairs_id=UUID(forex_pair_mapper.id),
                symbol=forex_pair_mapper.symbol,
                currency_group=forex_pair_mapper.currency_group,
                currency_base=forex_pair_mapper.currency_base,
                currency_quote=forex_pair_mapper.currency_quote,
            ),
            forex_pairs_mappers,
        )

        return list(forex_pairs_list)

    async def __domain_to_mappers(self, forex_pairs_list: List[ForexPairs]) -> List[ForexPairsMapper]:
        forex_pairs_mappers: Iterable[ForexPairsMapper] = map(
            lambda forex_pair: ForexPairsMapper(
                id=str(forex_pair.forex_pairs_id),
                symbol=forex_pair.symbol,
                currency_group=forex_pair.currency_group,
                currency_base=forex_pair.currency_base,
                currency_quote=forex_pair.currency_quote,
            ),
            forex_pairs_list,
        )

        return list(forex_pairs_mappers)
