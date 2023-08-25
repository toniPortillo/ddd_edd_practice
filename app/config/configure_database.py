from app.config.mapper_subscriber import mapper_subscriber
from app.config.database import Database


def configure_database(db: Database) -> Database:
    mapper_subscriber(db)
    
    return db
