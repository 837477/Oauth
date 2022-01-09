import requests


class FacebookOauth:
    def __init__(self, config):
        self.athorization_server = "https://www.facebook.com/v12.0/dialog/oauth"
        self.api_server = "https://graph.facebook.com/v12.0/oauth"
        self.client_id = config.FACEBOOK_CLIENT_ID
        self.secret_key = config.FACEBOOK_SECRET_KEY
        self.redirect_uri = config.FACEBOOK_REDIRECT_URI
        self.state = config.FACEBOOK_STATE

    def auth(self, code):
        """
        사용자로부터 전달 받은 Authorization code를 통하여,
        Access / Refresh Token 발행 요청
        """
        url = self.api_server + "/access_token?" \
                              + "client_id={}" \
                              + "&redirect_uri={}" \
                              + "&client_secret={}" \
                              + "&code={}"

        return requests.get(
            url=url.format(
                self.client_id,
                self.secret_key,
                self.redirect_uri,
                code
            )
        ).json()

    def url(self):
        url = self.athorization_server \
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

