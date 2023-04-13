from abc import ABC, abstractmethod
from typing import Dict, Optional, Tuple

from requests import Response


class HttpClient(ABC):
    @abstractmethod
    def get(
        self,
        path: str,
        headers: Optional[Dict] = None,
        timeout: Optional[Tuple[int, int]] = None,
        access_token_value: Optional[str] = None,
        language: Optional[str] = None,
    ) -> Response:
        pass
