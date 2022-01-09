from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from config import config
from controller.google import GoogleOauth
from controller.kakao import KakaoOauth
from controller.naver import NaverOauth


router = APIRouter()
templates = Jinja2Templates(directory="app/assets")


@router.get("/")
async def index(request: Request):
    """
    유저 인증 페이지인 Google oauth login URL을 전달.
    - 인증에 필요한 client_id / redirect_uri 정보를 이미 작성해둔 URL를 jinja를 통하여 전달.
    """
    google = GoogleOauth(config)
    kakao = KakaoOauth(config)
    naver = NaverOauth(config)
    context = {
        'request': request,
        'google': google.url(),
        'kakao': kakao.url(),
        'facebook': google.url(),
        'naver': naver.url()
    }
    print(context)
    return templates.TemplateResponse("index.html", context)
