from typing import Optional, Dict, Tuple
from common.infrastructure.client.http_client import HttpClient
from common.infrastructure.client.requests_session import RequestsSession

from requests import Response


class RequestsHttpClient(HttpClient):
    __TOKEN_TYPE = "Bearer"

    def __init__(
        self,
        session_requests: RequestsSession,
        url: str,
    ) -> None:
        self.session_requests = session_requests
        self.url = url

    def get(
        self,
        path: str,
        headers: Optional[Dict] = None,
        timeout: Optional[Tuple[int, int]] = None,
        access_token_value: Optional[str] = None,
        language: Optional[str] = None,
    ) -> Response:
        headers = self.__set_headers(headers, access_token_value, language)
        return self.session_requests.session_requests(
            url=self.url + path, method="get", headers=headers, timeout=timeout, retry_policy=None
        )

    def __set_headers(
        self,
        headers: Optional[Dict],
        access_token_value: Optional[str],
        language: Optional[str] = None,
    ) -> Dict:
        if headers is None:
            headers = {}
        if access_token_value is not None:
            headers["Authorization"] = f"{self.__TOKEN_TYPE} {access_token_value}"
        if language is not None:
            headers["Accept-Language"] = language
        return headers
