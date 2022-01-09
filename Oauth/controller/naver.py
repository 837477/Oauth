import requests


class NaverOauth:
    def __init__(self, config):
        self.athorization_server = "https://nid.naver.com/oauth2.0"
        self.api_server = "https://openapi.naver.com"
        self.client_id = config.NAVER_CLIENT_ID
        self.secret_key = config.NAVER_SECRET_KEY
        self.redirect_uri = config.NAVER_REDIRECT_URI
        self.state = config.NAVER_STATE

    def auth(self, code):
        """
        사용자로부터 전달 받은 Authorization code를 통하여,
        Access / Refresh Token 발행 요청 API
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
                "state": self.state,
                "code": code,
            }
        ).json()

    def refresh(self, refresh_token):
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
        url = self.athorization_server \
              + "/authorize" \
              + "?client_id={}" \
              + "&redirect_uri={}" \
              + "&state={}" \
              + "&response_type={}"
        return url.format(
            self.client_id,
            self.redirect_uri,
            self.state,
            "code"
        )

    def userinfo(self, access_token):
        return requests.get(
            url= self.api_server + "/v1/nid/me",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cache-Control": "no-cache",
                "Authorization": "Bearer " + access_token
            }
        ).json()
