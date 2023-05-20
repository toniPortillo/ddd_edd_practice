from uuid import UUID

from dataclasses import dataclass


@dataclass
class ForexPairs:
    id: UUID
    symbol: str
    currency_group: str
    currency_base: str
    currency_quote: str
