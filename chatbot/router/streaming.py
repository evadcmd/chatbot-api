# from typing import cast

from fastapi import APIRouter, WebSocket
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI

from chatbot.callback import ws

# from langchain.memory import ConversationBufferMemory


router = APIRouter(prefix="/api/v1/streaming")


@router.websocket("/chat")
async def streaming_chat(websocket: WebSocket):
    await websocket.accept()
    conversation = ConversationChain(llm=ChatOpenAI(streaming=True), verbose=True)  # type: ignore
    while True:
        data = await websocket.receive_text()
        await conversation.acall(data, callbacks=[ws.StreamingSendCallback(websocket)])
        # mem = cast(ConversationBufferMemory, conversation.memory)
        # print(mem.memory_variables[-1])
