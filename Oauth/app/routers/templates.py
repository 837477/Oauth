from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from config import config
from controller.google import GoogleOauth
from controller.kakao import KakaoOauth
from controller.naver import NaverOauth
from controller.facebook import FacebookOauth


router = APIRouter()
templates = Jinja2Templates(directory="app/assets")


@router.get("/")
async def index(request: Request):
    """
    사용자 인증 과정의 로그인 페이지인 Oauth login URL을 전달.
    """
    google = GoogleOauth(config)
    kakao = KakaoOauth(config)
    naver = NaverOauth(config)
    facebook = FacebookOauth(config)
    context = {
        'request': request,
        'google': google.url(),
        'kakao': kakao.url(),
        'facebook': facebook.url(),
        'naver': naver.url()
    }
    return templates.TemplateResponse("index.html", context)
