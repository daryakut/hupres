from contextvars import ContextVar

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from common.clock import now_ms
from common.env import env
from tests.users.sessions import get_test_session_data_provider
from users.session_data import SessionData

session_context_var: ContextVar[dict] = ContextVar("session", default={})


class SessionDataMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # This ensures every client gets a session cookies populated
        session_created_at = request.session.get("created_at", None)
        if not session_created_at:
            request.session["created_at"] = now_ms()

        # Set the session data in context var so that it can be accessed without requests
        session_context_var.set(request.session)
        return await call_next(request)


class SessionDataProvider:

    def get_current_session(self) -> SessionData:
        session = session_context_var.get()
        return SessionData(
            created_at=session.get("created_at"),
            user_token=session.get("user_token")
        )

    def update_current_session(self, user_token: str):
        session = session_context_var.get()
        session["user_token"] = user_token


session_data_provider = SessionDataProvider() if env.is_not_test() else get_test_session_data_provider()
