import os


class Dependencies:
    """Server Required Dependencies"""
    pass


class Config:
    DB_VERSION = 1
    
    APP_NAME = "Oauth"

    MONGODB_URI = os.environ[APP_NAME + "_MONGODB_URI"]
    MONGODB_NAME = os.environ[APP_NAME + "_MONGODB_NAME"]

    GOOGLE_CLIENT_ID = os.environ[APP_NAME + "_GOOGLE_CLIENT_ID"]
    GOOGLE_SECRET_KEY = os.environ[APP_NAME + "_GOOGLE_SECRET_KEY"]
    GOOGLE_API_KEY = os.environ[APP_NAME + "_GOOGLE_API_KEY"]
    GOOGLE_REDIRECT_URI = os.environ[APP_NAME + "_GOOGLE_REDIRECT_URI"]
