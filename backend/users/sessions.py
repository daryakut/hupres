from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from common.clock import now_ms


class SessionDataMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        session_created_at = request.session.get("created_at", None)
        if not session_created_at:
            request.session["created_at"] = now_ms()
        return await call_next(request)
