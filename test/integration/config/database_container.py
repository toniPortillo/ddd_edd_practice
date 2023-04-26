import os

from dependency_injector import containers, providers

from app.config.database import Database


class DatabaseContainer(containers.DeclarativeContainer):
    postgres_user: str = os.environ.get("DDD_EDD_PRACTICE_DB_USER")
    postgres_password: str = os.environ.get("DDD_EDD_PRACTICE_DB_PASSWORD")
    postgres_db_name: str = os.environ.get("TEST_DATABASE_NAME")
    postgres_db_port: str = os.environ.get("DDD_EDD_PRACTICE_DB_PORT")

    db_url: str = f"postgresql+psycopg2://{postgres_user}:{postgres_password}@db:{postgres_db_port}/{postgres_db_name}"
    
    db = providers.Singleton(
        Database, 
        db_url=db_url
    )
