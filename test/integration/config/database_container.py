from dependency_injector import containers, providers

from app.config.database import Database

class DatabaseContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['config.yml'])
    
    db = providers.Singleton(Database, db_url=config.database.dsn)
