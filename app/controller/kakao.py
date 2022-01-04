import requests


class KakaoOauth:    
    def __init__(self, config):
        self.auth_server = "https://kauth.kakao.com%s"
        self.api_server = "https://kapi.kakao.com%s"
        self.default_header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
        }
        self.client_id = config.GOOGLE_CLIENT_ID
        self.secret_key = config.GOOGLE_SECRET_KEY
        self.redirect_uri = config.GOOGLE_REDIRECT_URI

    def auth(self, code):
        return requests.post(
            url="https://kauth.kakao.com/oauth/token", 
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cache-Control": "no-cache",
            },
            data={
                "grant_type": "authorization_code",
                "client_id": self.client_id ,
                "client_secret": self.secret_key,
                "redirect_uri": self.redirect_uri,
                "code": code,
            }, 
        ).json()


    def refresh(self, refresh_token):
        return requests.post(
            url="https://kauth.kakao.com/oauth/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cache-Control": "no-cache",
            },
            data={
                "grant_type": "refresh_token",
                "client_id": self.client_id ,
                "client_secret": self.secret_key,
                "redirect_uri": self.redirect_uri,
            }, 
        ).json()
