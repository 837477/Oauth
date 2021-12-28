from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI
from model.mongodb import get_session


# Application Settings
app = FastAPI(
    docs_url="/documentation"
)
app.add_middleware(BaseHTTPMiddleware, dispatch=get_session)
app.add_middleware(SessionMiddleware, secret_key="Oauth!")


@app.on_event("startup")
async def startup():
    """Server Initialization"""
    print("Server Start ...")


@app.on_event("shutdown")
async def shutdown():
    """Server Clean-Up"""
    print("Server Shutdown ...")


# Routers Settings
from routers import templates
from routers.api import (
    google
)
app.include_router(templates.router)
app.include_router(google.router)
