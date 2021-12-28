from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from dependencies import Config
from controller.google import GoogleOauth


router = APIRouter()
templates = Jinja2Templates(directory="assets")


@router.get("/google")
async def index(request: Request):
    google = GoogleOauth(Config)
    context = {
        'request': request,
        'google': google.url(),
    }
    return templates.TemplateResponse("index.html", context)


@router.get("/oauth/")
async def oauth(code: str):
    google = GoogleOauth(Config)
    return google.auth(code)


@router.get("/oauth/refresh")
async def refresh(refresh_token: str):
    google = GoogleOauth(Config)
    return google.refresh(refresh_token)


@router.get("/userinfo")
async def userinfo(access_token: str):
    return GoogleOauth.userinfo(access_token)
