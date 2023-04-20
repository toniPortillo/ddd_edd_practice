import os
from dependency_injector import containers, providers

from app.config.database import Database


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['config.yml'])

    environment_db: str = os.environ.get('DDD_EDD_PRACTICE_DB_NAME')
    if os.environ.get('ENVIRONMENT') == 'test':
        environment_db = os.environ.get('TEST_DATABASE_NAME')
    postgres_user: str = os.environ.get('DDD_EDD_PRACTICE_DB_USER')
    postgres_password: str = os.environ.get('DDD_EDD_PRACTICE_DB_PASSWORD')
    postgres_port: str = int(os.environ.get('DDD_EDD_PRACTICE_DB_PORT'))
    db_url: str = f"postgresql+psycopg2://{postgres_user}:{postgres_password}@db:{postgres_port}/{environment_db}"
    db = providers.Singleton(
        Database, 
        db_url=db_url
    )
