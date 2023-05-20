from contextlib import contextmanager
from typing import Callable, ContextManager
import logging

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, Session

logger = logging.getLogger(__name__)

class Database:
    def __init__(self, db_url: str) -> None:
        self.__engine = create_engine(db_url, echo=True)
        self.__session_factory = scoped_session(
            sessionmaker(
                autocommit=False,
                expire_on_commit=False,
                autoflush=False,
                bind=self.__engine
            ),
        )
        self.__metadata = MetaData(bind=self.__engine)

    def create_database(self) -> None:
        self.__metadata.create_all(self.__engine)

    def drop_database(self) -> None:
        self.__metadata.drop_all(self.__engine)

    @property
    def metadata(self) -> MetaData:
        return self.__metadata

    @contextmanager
    def session(self) -> Callable[..., ContextManager[Session]]:
        session: Session = self.__session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()
