from fastapi import FastAPI

from chatbot.router import streaming

api = FastAPI(title="chatbot")
api.include_router(streaming.router)
