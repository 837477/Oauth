from fastapi import FastAPI
from app import routers
from app.routers import (templates,
                         google,
                         kakao,
                         naver,
                         facebook)


def create_app():
    """
    Application Creating
    """
    app = FastAPI(
        docs_url="/routers"
    )

    routers.init_app(app)

    # Routers Settings
    app.include_router(templates.router)
    app.include_router(google.router)
    app.include_router(kakao.router)
    app.include_router(naver.router)
    app.include_router(facebook.router)

    return app
