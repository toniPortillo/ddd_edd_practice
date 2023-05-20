from typing import Callable, ContextManager, List

from sqlalchemy.orm import Session

from forex_pairs.domain.forex_pairs import ForexPairs
from forex_pairs.domain.forex_pairs_repository import ForexPairsRepository


class SqlalchemyForexPairsRepository(ForexPairsRepository):
    def __init__(self, db_instance: Callable[..., ContextManager[Session]]):
        self.__db_instance = db_instance

    async def save_many(self, forex_pairs_list: List[ForexPairs]) -> int:
        with self.__db_instance() as session:
            session.add_all(forex_pairs_list)
            session.commit()
            return len(forex_pairs_list)

    async def find_all(self) -> List[ForexPairs]:
        with self.__db_instance() as session:
            query = session.query(ForexPairs)
            forex_pairs_list: List[ForexPairs] = query.all()
            return forex_pairs_list
