import time
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
