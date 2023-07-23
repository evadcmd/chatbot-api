import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

logger = logging.getLogger()


class Middleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start = time.time()
        response = await call_next(request)
        processing_time_ms = (time.time() - start) * 1000
        logger.info(
            "%s",
            {
                "method": request.method,
                "base_url": request.base_url,
                "path": request.scope.get("path", ""),
                "processing_time(ms)": processing_time_ms,
                "headers": dict(request.headers),
            },
        )
        return response
