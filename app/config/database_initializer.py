

class DatabaseInitializer:
    def __init__(self, engine, Base):
        self.__engine = engine
        self.__Base = Base

    async def initialize(self):
        self.__Base.metadata.create_all(bind=self.__engine)
