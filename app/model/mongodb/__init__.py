from fastapi import Request
from datetime import datetime
from pymongo import MongoClient
from dependencies import Dependencies, Config


async def get_session(request: Request, call_next):
    """Get MongoDB Client Cursor"""
    try:
        Dependencies.db = MongoClient(Config.MONGODB_URI)
        response = await call_next(request)
    finally:
        Dependencies.db.close()
    return response


class Model:
    def __init__(self, client: MongoClient, db_name=Config.MONGODB_NAME):
        self.col = client[db_name][self.__class__.__name__]

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


class DataManager:
    def __init__(self):
        self.db = MongoClient(Config.MONGODB_URI)
    
    def __del__(self):
        self.db.close()
