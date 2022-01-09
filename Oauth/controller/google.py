import requests


class GoogleOauth:
    def __init__(self, config):
        self.athorization_server = "https://accounts.google.com/o/oauth2/v2/auth"
        self.api_server = "https://oauth2.googleapis.com"
        self.client_id = config.GOOGLE_CLIENT_ID
        self.secret_key = config.GOOGLE_SECRET_KEY
        self.redirect_uri = config.GOOGLE_REDIRECT_URI

    def auth(self, code):
        """
        사용자로부터 전달 받은 Authorization code를 통하여,
        Access / Refresh Token 발행 요청 API
        """
        return requests.post(
            url=self.api_server + "/token",
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
        return requests.post(
            url=self.api_server + "/token",
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
              + "?scope={}" \
              + "&include_granted_scopes={}" \
              + "&response_type={}" \
              + "&state={}" \
              + "&access_type=offline" \
              + "&prompt=consent" \
              + "&redirect_uri={}" \
              + "&client_id={}"
        return url.format(
            "https://www.googleapis.com/auth/userinfo.email",
            "true",
            "code",
            "state_parameter_passthrough_value",
            self.redirect_uri,
            self.client_id
        )

    @staticmethod
    def userinfo(access_token):
        return requests.get(
            url="https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={}".format(
                access_token
            )
        ).json()
