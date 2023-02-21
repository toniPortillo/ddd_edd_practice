class ApplicationException(Exception):
    def __init__(
        self,
        standard_exception: str = "",
        exception_message: str = "",
    ) -> None:
        self.__standard_exception = standard_exception
        self.__exception_message = exception_message

    @property
    def standard_exception(
        self,
    ) -> str:
        return self.__standard_exception

    @property
    def exception_message(
        self,
    ) -> str:
        return self.__exception_message
