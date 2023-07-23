from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from chatbot.router import streaming

api = FastAPI(title="chatbot")
Instrumentator().instrument(api).expose(api)

api.include_router(streaming.router)
