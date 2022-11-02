from contextvars import ContextVar
from typing import Optional

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from common.clock import clock
from common.env import env
from models.token import generate_session_token, Token
from models.quiz_models import UserRole, User
from tests.users.fake_sessions import get_fake_session_data_provider
from users.session_data import SessionData

session_context_var: ContextVar[dict] = ContextVar("session", default={})



class SessionDataMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        session_data = request.session

        # This ensures every client gets a session cookies populated
        session_created_at = session_data.get("created_at", None)
        if not session_created_at:
            session_data["created_at"] = clock.now_ms()

        session_token = session_data.get("session_token", None)
        if not session_token:
            session_data["session_token"] = generate_session_token()

        # Set the session data in context var so that it can be accessed without request object reference
        session_context_var.set(session_data)
        return await call_next(request)


class SessionDataProvider:

    def get_current_session(self) -> SessionData:
        session = session_context_var.get()
        return SessionData(
            created_at=session.get("created_at"),
            session_token=session.get("session_token"),
            user_token=session.get("user_token")
        )

    def update_current_session(self, user_token: Optional[Token[User]], user_role: Optional[UserRole]):
        print(f"Logging in user {user_token}")
        session = session_context_var.get()
        session["user_token"] = user_token
        session["user_role"] = user_role


session_data_provider = SessionDataProvider() if env.is_not_test() else get_fake_session_data_provider()
