from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel

from database.db_models import DbUser
from database.transaction import transaction
from quiz_algorithm.models import User, UserRole
from users.google_oauth import google_oauth, GOOGLE_AUTH_CALLBACK_PATH, decode_id_token_email_address
import re

from users.sessions import update_current_session

router = APIRouter()


ADMIN_USER_EMAIL_ADDRESSES = [
    "olgeorge@gmail.com",
]


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

    # Google ignores dots in email addresses
    sanitized_email_address = re.sub(r'\+[^@]*@', '@', email_address.replace(".", ""))
    with transaction() as session:
        existing_users = session.query(User).filter(User.email_address == sanitized_email_address).all()
        if len(existing_users) == 0:
            role = UserRole.ADMIN if sanitized_email_address in ADMIN_USER_EMAIL_ADDRESSES else UserRole.RESPONDENT
            db_user = DbUser.create_user(session, email_address=sanitized_email_address, role=role)
            user_token = db_user.user_token
        elif len(existing_users) == 1:
            db_user = existing_users[0]
            user_token = db_user.user_token
        else:
            raise Exception(f"Multiple users with email address {sanitized_email_address}")

    update_current_session(user_token)
    return {"email": email_address, "user_token": user_token}


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
