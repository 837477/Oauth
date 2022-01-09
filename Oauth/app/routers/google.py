from fastapi import APIRouter
from config import config
from controller.google import GoogleOauth


router = APIRouter(
    prefix="/google"
)


@router.get("/oauth/")
async def oauth(code: str):
    """
    사용자로부터 Authorization code를 인자로 받는다.
    (정확하게는, 다음과 같은 시퀀스를 가진다.)
    - /google 을 통하여 전달받은 url로 접속을하면 Google Login 폼이 뜬다.
    - 여기서 Google 로그인을 진행
    - 그러면, Google Cloud Platform 에 미리 설정해둔 Redirect uri로 Authorization Code가 전달됨.
    - 설정해둔 Redirect uri가 본 함수인 /ouath 임.

    Authorization Code를 전달받은 본 API는 다음과 같은 과정을 수행.
    1. Authorization code를 다시 Google 서버에 요청을하여, Access / Refresh Token을 발급
    2. Access Token를 Google API에 전달하여, 사용자 정보 획득
    3. 해당 사용자 정보를 DB에 저장 (만약, 이미 DB에 존재하면 Skip)
    4. 사용자 식별 ID를 통하여 본 서비스의 JWT Access Token을 생성
    """
    google = GoogleOauth(config)
    return google.auth(code)


@router.get("/oauth/refresh")
async def refresh(refresh_token: str):
    """
    Refresh Token을 통하여 Access Token 재발급

    Query Parameter을 통하여 Refresh Token을 전달하면,
    새로운 Access Token이 발급됨.
    """
    google = GoogleOauth(config)
    return google.refresh(refresh_token)


@router.get("/userinfo")
async def userinfo(access_token: str):
    """
    Access Token을 통하여 User information을 반환

    Query Parameter을 통하여 Access Token을 전달하면,
    사용자 정보를 반환.
    """
    return GoogleOauth.userinfo(access_token)
