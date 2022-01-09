from datetime import datetime
from pymongo import MongoClient
from config import Config


class Model:
    def __init__(self):
        self.db = MongoClient(Config.MONGODB_URI)
        self.col = self.db[Config.MONGODB_NAME][self.__class__.__name__]

    @property
    def schema(self) -> dict:
        return {
            '_created': datetime.now(),
            '_updated': datetime.now(),
            '_version': Config.DB_VERSION
        }
    
    def schemize(self, document: dict) -> dict:
        """Generate JSON scheme"""
        return {**self.schema, **document}

    def __del__(self):
        self.db.close()
