from typing import Optional, Dict, Tuple, Union
from requests import Response, Session
from requests.adapters import HTTPAdapter, Retry


class RequestsSession:
    __DEFAULT_TIMEOUT = (2, 10)
    __DEFAULT_RETRY_POLICY = Retry(
        total=3,
        backoff_factor=0.6,
        status_forcelist=[502, 504],
        method_whitelist=frozenset(["GET"]),
    )

    @classmethod
    def session_requests(
        cls,
        url: str,
        method: str,
        headers: Optional[Dict],
        timeout: Optional[Tuple[int, int]],
        retry_policy: Optional[Retry],
        **kwargs: Union[Optional[Dict], Optional[str]],
    ) -> Response:
        if retry_policy is None:
            retry_policy = cls.__DEFAULT_RETRY_POLICY

        session: Session = Session()
        session.mount(url, HTTPAdapter(max_retries=retry_policy))

        data = kwargs.get("data")
        json = kwargs.get("json")

        if timeout is None:
            timeout = cls.__DEFAULT_TIMEOUT

        if data is not None or json is not None:
            response = session.request(url=url, method=method, headers=headers, timeout=timeout, data=data, json=json)
        else:
            response = session.request(url=url, method=method, headers=headers, timeout=timeout)

        return response
