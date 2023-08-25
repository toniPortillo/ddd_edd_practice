import uuid

from dataclasses import dataclass


@dataclass
class ForexPairs:
    id: uuid.UUID
    symbol: str
    currency_group: str
    currency_base: str
    currency_quote: str
