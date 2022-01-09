import requests


class KakaoOauth:
    def __init__(self, config):
        self.athorization_server = "https://kauth.kakao.com/oauth"
        self.api_server = "https://kapi.kakao.com"
        self.client_id = config.KAKAO_CLIENT_ID
        self.secret_key = config.KAKAO_SECRET_KEY
        self.redirect_uri = config.KAKAO_REDIRECT_URI

    def auth(self, code):
        """
        사용자로부터 전달 받은 Authorization code를 통하여,
        Access / Refresh Token 발행 요청
        """
        return requests.post(
            url=self.athorization_server + "/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cache-Control": "no-cache",
            },
            data={
                "grant_type": "authorization_code",
                "client_id": self.client_id,
                "client_secret": self.secret_key,
                "redirect_uri": self.redirect_uri,
                "code": code,
            }
        ).json()

    def refresh(self, refresh_token):
        """
        Refresh Token을 통하여, 새로운 Access Token 발행 요청
        """
        return requests.post(
            url=self.athorization_server + "/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cache-Control": "no-cache",
            },
            data={
                "grant_type": "refresh_token",
                "client_id": self.client_id,
                "client_secret": self.secret_key,
                "refresh_token": refresh_token
            }
        ).json()

    def url(self):
        """
        사용자 측에서 접속 할 URL 생성
        """
        url = self.athorization_server \
              + "/authorize" \
              + "?client_id={}" \
              + "&redirect_uri={}" \
              + "&response_type={}"
        return url.format(
            self.client_id,
            self.redirect_uri,
            "code"
        )

    def userinfo(self, access_token):
        """
        Access Token을 통하여, 사용자 Information 요청
        """
        return requests.get(
            url= self.api_server + "/v2/user/me",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cache-Control": "no-cache",
                "Authorization": "Bearer " + access_token
            }
        ).json()
