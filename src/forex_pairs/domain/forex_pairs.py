from dataclasses import dataclass


@dataclass
class ForexPairs:
    forex_pairs_id: str
    symbol: str
    currency_group: str
    currency_base: str
    currency_quote: str
