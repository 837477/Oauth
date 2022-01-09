from os import environ
from dataclasses import dataclass


@dataclass
class Config:
    """
    Configuration
    """
    APP_NAME: str = "Oauth"
    APP_VERSION: float = 1.0
    DB_VERSION: float = 1.0

    BASE_API_TIME: float = 0.5

    JWT_SECRET_KEY: str = environ[APP_NAME + "_JWT_SECRET_KEY"]
    JWT_ALGORITHM: str = "HS256"

    MONGODB_URI: str = environ[APP_NAME + "_MONGODB_URI"]
    MONGODB_NAME: str = environ[APP_NAME + "_MONGODB_NAME"]

    # Google Info
    GOOGLE_CLIENT_ID: str = environ[APP_NAME + "_GOOGLE_CLIENT_ID"]
    GOOGLE_SECRET_KEY: str = environ[APP_NAME + "_GOOGLE_SECRET_KEY"]
    GOOGLE_REDIRECT_URI: str = environ[APP_NAME + "_GOOGLE_REDIRECT_URI"]

    # Kakao Info
    KAKAO_CLIENT_ID: str = environ[APP_NAME + "_KAKAO_CLIENT_ID"]
    KAKAO_SECRET_KEY: str = environ[APP_NAME + "_KAKAO_SECRET_KEY"]
    KAKAO_REDIRECT_URI: str = environ[APP_NAME + "_KAKAO_REDIRECT_URI"]

    # Naver Info
    NAVER_CLIENT_ID: str = environ[APP_NAME + "_NAVER_CLIENT_ID"]
    NAVER_SECRET_KEY: str = environ[APP_NAME + "_NAVER_SECRET_KEY"]
    NAVER_REDIRECT_URI: str = environ[APP_NAME + "_NAVER_REDIRECT_URI"]
    NAVER_STATE: str = environ[APP_NAME + "_NAVER_STATE"]

    # Facebook Info
    FACEBOOK_CLIENT_ID: str = environ[APP_NAME + "_FACEBOOK_CLIENT_ID"]
    FACEBOOK_SECRET_KEY: str = environ[APP_NAME + "_FACEBOOK_SECRET_KEY"]
    FACEBOOK_REDIRECT_URI: str = environ[APP_NAME + "_FACEBOOK_REDIRECT_URI"]
    FACEBOOK_STATE: str = environ[APP_NAME + "_FACEBOOK_STATE"]

@dataclass
class LocalConfig(Config):
    """
    Local(Testing) Configuration
    """
    RELOAD: bool = True
    PORT: int = 8000
    LOGGING: bool = False


@dataclass
class ProductionConfig(Config):
    """
    Production Configuration
    """
    RELOAD: bool = False
    PORT: int = 80
    LOGGING: bool = True


configs = {
    "production": ProductionConfig(),
    "local": LocalConfig()
}
config = configs[environ.get((Config.APP_NAME + "_CONFIG"), "local")]
