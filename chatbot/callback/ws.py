from typing import Any
from uuid import UUID

from fastapi import WebSocket
from langchain.callbacks.base import AsyncCallbackHandler


class StreamingSendCallback(AsyncCallbackHandler):
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket

    async def on_llm_new_token(
        self,
        token: str,
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        tags: list[str] | None = None,
        **kwargs: Any,
    ) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        await self.websocket.send_text(token)
