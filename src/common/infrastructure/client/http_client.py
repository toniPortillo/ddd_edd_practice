from abc import ABC, abstractmethod

from requests import Response


class HttpClient(ABC):
    @abstractmethod
    def get(self) -> Response:
        pass

    @abstractmethod
    def post(self) -> Response:
        pass

    @abstractmethod
    def patch(self) -> Response:
        pass
