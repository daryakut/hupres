"""
Application definition
"""
import json
import os

import httpx
from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlalchemy import func
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request

from database.db_models import DbUser
from database.transaction import transaction
from quiz_algorithm.models import Quiz, User, UserRole


# Manually fetch the server metadata to fix the issuer
response = httpx.get('https://accounts.google.com/.well-known/openid-configuration')
metadata = response.json()
# The issuer in the metadata is wrong. It is 'https://accounts.google.com' but should be 'accounts.google.com'
metadata['issuer'] = 'accounts.google.com'

oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.environ['HUPRES_GOOGLE_0AUTH_CLIENT_ID'],
    client_secret=os.environ['HUPRES_GOOGLE_0AUTH_CLIENT_SECRET'],
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='https://f4d9-2607-fea8-86e5-fc00-2457-6377-7d54-1aff.ngrok-free.app/auth',
    client_kwargs={'scope': 'openid profile email'},
    # server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    **metadata,
)
# oauth.google.client_metadata['issuer'] = 'accounts.google.com'

app = FastAPI()

# This is important for OAuth2 to store temporary state
app.add_middleware(SessionMiddleware, secret_key=os.environ['HUPRES_SECRET_SESSION_KEY'])


@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth")
async def auth(request: Request):
    # print("request", request.__dir__())

    token = await oauth.google.authorize_access_token(request)
    print(f"token {token}")
    #
    # # Fetch the user's profile
    # user = await oauth.google.parse_id_token(request, token)
    # print(f"user {user}")
    #
    # # Here you can create a user session or do whatever you'd like
    # return {"email": user['email'], "name": user['name']}


@app.get("/set-session")
def set_session(request: Request):
    request.session["message"] = "Hello, World!"
    return {"status": "session set"}


@app.get("/get-session")
def get_session(request: Request):
    return {"session_value": request.session.get("message")}


# # Base = declarative_base()
#
# # class User(Base):
# #     __tablename__ = 'users'
# #     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
# #     name = Column(String(50))
# #     age = Column(Integer)
#
# DATABASE_URL = "postgresql+psycopg2://georgii:@localhost/georgii"
#
# engine = create_engine(DATABASE_URL)
#
# # Create tables in the database (only need to run this once)
# # Base.metadata.create_all(engine)
#
# # To start a new session and interact with the database
# Session = sessionmaker(bind=engine)
# session = Session()


@app.get("/")
async def home():
    with transaction() as session:
        current_timestamp = session.query(func.now()).scalar()
        return HTMLResponse(f"Hello world! {current_timestamp}")
    # return HTMLResponse("Hello world!")


@app.get("/404")
async def missing():
    return HTMLResponse("That's gonna be a 'no' from me.", status_code=404)


class CreateQuizResponse(BaseModel):
    quiz: Quiz


@app.post("/quizzes")
async def create_quiz() -> CreateQuizResponse:
    return CreateQuizResponse(quiz=Quiz())


class UserSignupRequest(BaseModel):
    email_address: str


class UserSignupResponse(BaseModel):
    user: User


@app.post("/users/signup")
async def user_signup(request: UserSignupRequest) -> UserSignupResponse:
    with transaction() as session:
        db_user = DbUser.create_user(session, email_address=request.email_address, role=UserRole.RESPONDENT)
        return UserSignupResponse(user=db_user.to_model())


@app.post("/auth/callback")
async def auth_callback(request):
    print(f"Received 0Auth callback: {json.dumps(request)}")
