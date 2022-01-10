import time
import jwt
from fastapi import FastAPI, Request
from config import config
from model.mongodb.log import Log


def init_app(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        pass

    @app.on_event("shutdown")
    async def shutdown():
        pass

    @app.middleware("http")
    async def process_time_logging(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        # Slow API Print
        if process_time > config.BASE_API_TIME:
            log_str = "\n[Slow API Detected]\n" + \
                  "Host: " + request.client.host + "\n" + \
                  "Url: " + request.url.path + "\n" + \
                  "Path Params: " + str(request.path_params) + "\n" + \
                  "Execute Time: " + str(process_time) + "\n"
            print(log_str)

        # Slow API Logging
        if config.LOGGING:
            log_document = {
                "host": request.client.host,
                "url": request.url.path,
                "path_params": request.path_params,
                "execute_time": str(process_time)
            }
            Log().insert_log(document=log_document)

        return response


def encode_jwt(user: dict):
    return jwt.encode(
        payload={
            **user,
            **{"expires": time.time() + config.JWT_EXPIRES}
        },
        key=config.JWT_SECRET_KEY,
        algorithm=config.JWT_ALGORITHM
    )


def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(
            jwt=token,
            key=config.JWT_SECRET_KEY,
            algorithms=config.JWT_ALGORITHM
        )
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return False
