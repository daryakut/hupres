import os
from contextvars import ContextVar
from typing import Optional

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from common.clock import clock
from common.env import env
from models.token import generate_session_token, Token
from models.user import User
from models.user_role import UserRole
from tests.users.fake_sessions import get_fake_session_data_provider
from users.session_data import SessionData

session_context_var: ContextVar[dict] = ContextVar("session", default={})

SESSION_MIDDLEWARE_CONFIG = {
    'secret_key': os.environ['HUPRES_SECRET_SESSION_KEY'],
    'session_cookie': 'hupres_session',
    'same_site': 'none',
}


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
        # return await call_next(request)

        response = await call_next(request)

        # # Create the cookie
        # cookie = SimpleCookie()
        # cookie['session_id'] = session_data['session_token']
        # cookie['session_id']['httponly'] = True
        # cookie['session_id']['samesite'] = 'None'
        # cookie['session_id']['secure'] = True  # Secure flag, required if SameSite=None
        # cookie['session_id']['path'] = '/'
        # # if 'DOMAIN' in os.environ:
        # #     cookie['session_id']['domain'] = os.environ['DOMAIN']
        #
        # # Set the 'Set-Cookie' header
        # response.headers.append(
        #     'Set-Cookie',
        #     cookie['session_id'].OutputString(),
        # )

        return response


class SetCookieMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Here we're setting a cookie named 'session_id' as an example
        # You should set your actual session token and handle its generation accordingly
        session_token = "example-session-token"

        response.set_cookie(
            key="session",
            value=session_token,
            httponly=True,  # Helps mitigate XSS attacks by not exposing the cookie to JS
            samesite='none',  # Set SameSite attribute to None
            secure=True,  # Set Secure, mandatory for SameSite=None
        )

        return response


class SessionDataProvider:

    def get_current_session(self) -> SessionData:
        session = session_context_var.get()
        user_token = session.get("user_token")
        user_role = session.get("user_role")
        return SessionData(
            created_at=session.get("created_at"),
            session_token=session.get("session_token"),
            user_token=Token.of(session.get("user_token")) if user_token else None,
            user_role=UserRole(user_role) if user_role else None,
        )

    def update_current_session(self, user_token: Optional[Token[User]], user_role: Optional[UserRole]):
        print(f"Logging in user {user_token}")
        session = session_context_var.get()
        session["user_token"] = user_token.value if user_token else None
        session["user_role"] = user_role.value if user_role else None


session_data_provider = SessionDataProvider() if env.is_not_test() else get_fake_session_data_provider()
