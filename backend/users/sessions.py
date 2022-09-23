
import os

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.sessions import SessionMiddleware

from common.clock import now_ms
from main.fast_api_app import app


class SessionDataMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        session_created_at = request.session.get("created_at", None)
        if not session_created_at:
            request.session["created_at"] = now_ms()
        return await call_next(request)


app.add_middleware(SessionDataMiddleware)
app.add_middleware(SessionMiddleware, secret_key=os.environ['HUPRES_SECRET_SESSION_KEY'])

