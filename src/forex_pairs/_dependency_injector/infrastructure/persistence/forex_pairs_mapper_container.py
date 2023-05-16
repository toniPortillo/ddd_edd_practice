from dependency_injector import containers, providers

from src.forex_pairs.infrastructure.persistence.forex_pairs_mapper import ForexPairsMapper


class ForexPairsMapperContainer(containers.DeclarativeContainer):
    db_instance = providers.Dependency()

    forex_pairs_mapper = providers.Factory(
        ForexPairsMapper,
        db_instance=db_instance,
    )
