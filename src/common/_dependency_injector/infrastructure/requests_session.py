from dependency_injector import containers, providers

from common.infrastructure.client.requests_session import RequestsSession


class RequestsSessionContainer(containers.DeclarativeContainer):
    requests_session = providers.Singleton(
        RequestsSession,
    )
