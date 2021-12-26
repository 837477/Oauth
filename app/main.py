from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI
from model.mongodb import get_session


# Application Settings
app = FastAPI(
    docs_url="/documentation"
)
app.add_middleware(BaseHTTPMiddleware, dispatch=get_session)


@app.on_event("startup")
async def startup():
    """Server Initialization"""
    print("Server Start ...")


@app.on_event("shutdown")
async def shutdown():
    """Server Clean-Up"""
    print("Server Shutdown ...")


# Routers Settings
from routers import (
    templates
)
app.include_router(templates.router)
