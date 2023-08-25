from typing import Type

from sqlalchemy import Column, String, Table
from sqlalchemy.dialects.postgresql import UUID

from src.common.infrastructure.persistence.mapper import Mapper
from src.forex_pairs.domain.forex_pairs import ForexPairs


class ForexPairsMapper(Mapper):
    def table(self) -> Table:
        forex_pairs_table = Table(
            "forex_pairs",
            self._db_instance.metadata,
            Column("id", UUID(as_uuid=True), primary_key=True, nullable=False),
            Column("symbol", String(), nullable=False),
            Column("currency_group", String(), nullable=False),
            Column("currency_base", String(), nullable=False),
            Column("currency_quote", String(), nullable=False),
        )

        return forex_pairs_table

    def entity(self) -> Type:
        return ForexPairs
