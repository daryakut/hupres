from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel

from database.db_models import DbUser
from database.transaction import transaction
from quiz_algorithm.models import User, UserRole
from users.google_oauth import google_oauth, GOOGLE_AUTH_CALLBACK_PATH, decode_id_token_email_address

router = APIRouter()


@router.get("/users/google-login")
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await google_oauth.google.authorize_redirect(request, redirect_uri)


@router.get(GOOGLE_AUTH_CALLBACK_PATH)
async def auth(request: Request):
    token = await google_oauth.google.authorize_access_token(request)
    print(f"token {token}")

    email_address = decode_id_token_email_address(token)
    print(f"email_address {email_address}")

    return {"email": email_address}


# @router.get("/set-session")
# def set_session(request: Request):
#     request.session["message"] = "Hello, World!"
#     return {"status": "session set"}
#
#
# @router.get("/get-session")
# def get_session(request: Request):
#     return {"session_value": request.session.get("message")}


class UserSignupRequest(BaseModel):
    email_address: str


class UserSignupResponse(BaseModel):
    user: User


@router.post("/users/signup")
async def user_signup(request: UserSignupRequest) -> UserSignupResponse:
    with transaction() as session:
        db_user = DbUser.create_user(session, email_address=request.email_address, role=UserRole.RESPONDENT)
        return UserSignupResponse(user=db_user.to_model())
