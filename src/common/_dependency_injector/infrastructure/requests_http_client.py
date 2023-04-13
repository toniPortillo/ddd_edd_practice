from dependency_injector import containers, providers

from common.infrastructure.client.requests_http_client import RequestsHttpClient


class RequestsHttpClientContainer(containers.DeclarativeContainer):
    requests_session = providers.Dependency()
    url = providers.Dependency()

    requests_http_client = providers.Singleton(
        RequestsHttpClient,
        requests_session,
        url,
    )
