import os


class Dependencies:
    """Server Required Dependencies"""
    pass


class Config:
    DB_VERSION = 1
    
    APP_NAME = "_837477"

    MONGODB_URI = os.environ[APP_NAME + "_MONGODB_URI"]
    MONGODB_NAME = os.environ[APP_NAME + "_MONGODB_NAME"]
