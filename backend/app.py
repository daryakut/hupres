"""
Application definition
"""

import os

from fastapi import Request, FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import func
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.sessions import SessionMiddleware

import quizzes.quizzes_api
import users.users_api
from main.fast_api_app import app
from common.clock import now_ms
from database.transaction import transaction


class SessionDataMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        session_created_at = request.session.get("created_at", None)
        if not session_created_at:
            request.session["created_at"] = now_ms()
        return await call_next(request)

# app = FastAPI()

app.add_middleware(SessionDataMiddleware)
app.add_middleware(SessionMiddleware, secret_key=os.environ['HUPRES_SECRET_SESSION_KEY'])


app.include_router(users.users_api.router, tags=["users"])
app.include_router(quizzes.quizzes_api.router, tags=["quizzes"])

@app.get("/")
async def home():
    return HTMLResponse("Hello world!")


@app.get("/time")
async def home():
    with transaction() as session:
        current_timestamp = session.query(func.now()).scalar()
        return HTMLResponse(f"Hello world! {current_timestamp}")
    # return HTMLResponse("Hello world!")


@app.get("/404")
async def missing():
    return HTMLResponse("That's gonna be a 'no' from me.", status_code=404)
