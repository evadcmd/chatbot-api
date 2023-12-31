from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from chatbot.middleware import accesslogger
from chatbot.router import streaming

api = FastAPI(title="chatbot")
Instrumentator().instrument(api).expose(api)

api.include_router(streaming.router)
api.add_middleware(accesslogger.Middleware)
