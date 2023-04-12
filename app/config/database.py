from contextlib import contextmanager, AbstractContextManager
from typing import Callable, TypeVar, ContextManager
import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, Session

T = TypeVar('T')

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:
    def __init__(self, db_url: str) -> None:
        self.__engine = create_engine(db_url, echo=True)
        self.__session_factory = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.__engine
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self.__engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self.__session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()
