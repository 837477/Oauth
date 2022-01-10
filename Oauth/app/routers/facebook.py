from fastapi import APIRouter
from config import config
from controller.facebook import FacebookOauth


router = APIRouter(
    prefix="/facebook"
)


@router.get("/oauth/")
async def oauth(code: str):
    """
    사용자로부터 Authorization code를 인자로 받는다.
    (정확하게는, 해당 플랫폼의 Authorization server에서 Redirect하여 반환해준 값)
    - Home에서 Facebook Login 폼으로 url 이동
    - 로그인 진행(완료)
    - Facebook Developer 에 미리 설정 해 놓은 Redirect uri로 Authorization Code가 전달됨.
    - 설정해둔 Redirect uri가 본 함수인 /ouath 임.

    Authorization Code를 전달받은 본 API는 다음과 같은 과정을 수행.
    1. Authorization code를 다시 Facebook 서버에 요청을하여, Access / Refresh Token을 발급
    2. Access Token를 Facebook API에 전달하여, 사용자 정보 획득
    3. 해당 사용자 정보를 DB에 저장 (만약, 이미 DB에 존재하면 Skip)
    4. 사용자 식별 ID를 통하여 본 서비스의 JWT Access Token을 생성
    5. 발행된 JWT를 Cookie 등록 / 반환 (원래의 페이지로 Redirection)

    현재 Facebook은 redirect_uri가 https 인증이 되어있어야 테스트가 가능하다.
    (SSL 인증이 필요하므로 잠시 테스트 보류)
    """
    facebook = FacebookOauth(config)
    return facebook.auth(code)
