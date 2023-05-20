from typing import Type

from sqlalchemy import Column, String, Table
from sqlalchemy.dialects.postgresql import UUID

from src.common.infrastructure.persistence.mapper import Mapper
from src.forex_pairs.domain.forex_pairs import ForexPairs


class ForexPairsMapper(Mapper):
    __table = None

    def table(self) -> Table:
        if self.__table is None:
            self.__table = Table(
                "forex_pairs",
                self._db_instance.metadata,
                Column("id", UUID(as_uuid=False), primary_key=True, nullable=False),
                Column("symbol", String(), nullable=False),
                Column("currency_group", String(), nullable=False),
                Column("currency_base", String(), nullable=False),
                Column("currency_quote", String(), nullable=False),
            )

        return self.__table

    def entity(self) -> Type:
        return ForexPairs
