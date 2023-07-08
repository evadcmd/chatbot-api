from fastapi import APIRouter, WebSocket

from chatbot.callback import ws
from chatbot.llm.openai import conversation

router = APIRouter(prefix="/api/streaming")


@router.websocket("/chat")
async def streamng_chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await conversation.acall(data, callbacks=[ws.AsyncSendCallback(websocket)])
