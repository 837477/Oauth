# Oauth 2.0 Login
__Google (구현 완료): [Refer Here](https://developers.google.com/identity/protocols/oauth2/web-server)__ <br>
__Apple (보류 - Apple Developer 등록)__ <br>
__Facebook (보류 - HTTPS 인증 이슈): [Refer Here](https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow?locale=ko_KR)__ <br>
__Kakao (구현 완료): [Refer Here](https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api)__ <br>
__Naver (구현 완료): [Refer Here](https://developers.naver.com/docs/login/api/api.md)__ <br>
<br><br>

<div align=center>
    <strong># FastAPI</strong> &nbsp;
    <strong># Oauth 2.0</strong> &nbsp;
</div>
<br>

## What is this?
Python을 이용한, 다양한 플랫폼 Oauth 2.0 Login 모듈 예제입니다.<br>
테스트에 사용된 프레임워크는 FastAPI이지만, Oauth 기능은 FastAPI에 종속되지 않았기 때문에 타 환경에서도 사용 가능합니다.

Oauth 인증 방식은 대부분의 플랫폼이 비슷한 방식을 하나의 규칙처럼 사용하고 있습니다.<br>
따라서, 아직 Apple / Facebook 의 Oauth Login은 개발자 등록(비용 문제) 및 HTTPS SSL 인증 등으로 인하여 미구현 상태이지만, 내부 방식은 비슷할 것으로 예상됩니다.

현재 본 Repo에서 테스트 가능한 플랫폼은 Google / Kakao / Naver 입니다.
<br><br>

## Dependency
본 예제 코드를 실행하기 위해서는, 먼저 각 플랫폼의 Developer 관리자에서 Application 등록을 완료해야 합니다.<br>
그 후, 발급 받은 Client_id / Client_secret / Redirect_URI 등의 정보를 config.py에 저장해주세요.<br>
(보안상의 문제로 환경 변수를 사용하는 것을 권장드립니다.)

또한, 본 예제 코드는 [837477/FastAPI-Pymongo](https://github.com/837477/FastAPI-Pymongo) 구조를 기반으로 구현되었기 때문에 해당 Repo의 Dependency를 따라야합니다.

개별적으로 실행시키기 위해서는 Oauth 인증 Key들만 따로 분리하여 Controller의 google.py / kakao.py / naver.py 를 사용해주세요.
```shell
# 다음의 값은 실제 값이 아닌 임의의 값을 입력한 예시 입니다.
export Oauth_GOOGLE_CLIENT_ID="198f75998f7dc4f1198f75970400f56.apps.googleusercontent.com"
export Oauth_GOOGLE_SECRET_KEY="vQwYiNVqGOCSiOugBu9UFPX-ieqM7TReLYc"
export Oauth_GOOGLE_REDIRECT_URI="http://localhost:8000/google/oauth"

export Oauth_KAKAO_CLIENT_ID="d1fbea86f1ln1nfa635c8fe84b62e7c9b81"
export Oauth_KAKAO_SECRET_KEY="MGssdfcPjcCjl304zoMWPp9JOdRrxS4lgg"
export Oauth_KAKAO_REDIRECT_URI="http://localhost:8000/kakao/oauth"

export Oauth_NAVER_CLIENT_ID="rVHfUq1obb48abbsda41x0X"
export Oauth_NAVER_SECRET_KEY="hyfek_DT43"
export Oauth_NAVER_REDIRECT_URI="http://localhost:8000/naver/oauth"
export Oauth_NAVER_STATE="RANDOM STATE"

export Oauth_FACEBOOK_CLIENT_ID="112874087512345124"
export Oauth_FACEBOOK_SECRET_KEY="f430fb12401gb0108br26fad3a8cdeea6ae"
export Oauth_FACEBOOK_REDIRECT_URI="https://localhost:8000/facebook/oauth"
export Oauth_FACEBOOK_STATE="RANDOM STATE"
```
```python
# config.py 의 Config Class

# Google Info
GOOGLE_CLIENT_ID: str = environ[APP_NAME + "_GOOGLE_CLIENT_ID"]
GOOGLE_SECRET_KEY: str = environ[APP_NAME + "_GOOGLE_SECRET_KEY"]
GOOGLE_REDIRECT_URI: str = environ[APP_NAME + "_GOOGLE_REDIRECT_URI"]

# Kakao Info
KAKAO_CLIENT_ID: str = environ[APP_NAME + "_KAKAO_CLIENT_ID"]
KAKAO_SECRET_KEY: str = environ[APP_NAME + "_KAKAO_SECRET_KEY"]
KAKAO_REDIRECT_URI: str = environ[APP_NAME + "_KAKAO_REDIRECT_URI"]

# Naver Info
NAVER_CLIENT_ID: str = environ[APP_NAME + "_NAVER_CLIENT_ID"]
NAVER_SECRET_KEY: str = environ[APP_NAME + "_NAVER_SECRET_KEY"]
NAVER_REDIRECT_URI: str = environ[APP_NAME + "_NAVER_REDIRECT_URI"]
NAVER_STATE: str = environ[APP_NAME + "_NAVER_STATE"]

# Facebook Info
FACEBOOK_CLIENT_ID: str = environ[APP_NAME + "_FACEBOOK_CLIENT_ID"]
FACEBOOK_SECRET_KEY: str = environ[APP_NAME + "_FACEBOOK_SECRET_KEY"]
FACEBOOK_REDIRECT_URI: str = environ[APP_NAME + "_FACEBOOK_REDIRECT_URI"]
FACEBOOK_STATE: str = environ[APP_NAME + "_FACEBOOK_STATE"]
```
```shell
python 3.8.X
```
<br>

## How to use
```shell
pip install -r requirements.txt
python3 main.py
```
<br>

## Contributor
🙋🏻‍♂️ Name: [837477](https://837477.github.io)

📧 E-mail: 8374770@gmail.com

🐱 Github: https://github.com/837477

<br>

## Contributing
1. Fork this repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

