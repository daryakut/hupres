import re

from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel

from database.db_user import DbUser
from database.transaction import transaction
from quiz_algorithm.models import User, UserRole
from users.google_oauth import GOOGLE_AUTH_CALLBACK_PATH, google_oauth_service
from users.sessions import session_data_provider

router = APIRouter()

ADMIN_USER_EMAIL_ADDRESSES = [
    "olgeorgeacc@gmail.com",
]


@router.get(GOOGLE_AUTH_CALLBACK_PATH)
async def google_auth(request: Request):
    email_address = await google_oauth_service.authorize_access_token_and_get_email_address(request)

    # Google ignores dots in email addresses
    email_first_part, email_second_part = email_address.split("@")
    address_without_dots = email_first_part.replace(".", "") + "@" + email_second_part
    sanitized_email_address = re.sub(r'\+[^@]*@', '@', address_without_dots)
    print('sanitized_email_address', sanitized_email_address)
    with transaction() as session:
        existing_users = DbUser.find_all_by_email_address(session, sanitized_email_address)
        print('existing_users', existing_users)
        if len(existing_users) == 0:
            role = UserRole.ADMIN if sanitized_email_address in ADMIN_USER_EMAIL_ADDRESSES else UserRole.RESPONDENT
            db_user = DbUser.create_user(session, email_address=sanitized_email_address, role=role)
            user_token = db_user.token
        elif len(existing_users) == 1:
            db_user = existing_users[0]
            user_token = db_user.token
        else:
            raise Exception(f"Multiple users with email address {sanitized_email_address}")

    session_data_provider.update_current_session(user_token)
    return {"email": email_address, "user_token": user_token}


@router.get("/users/google-login")
async def google_login(request: Request):
    # This is http://localhost:8000/users/google-auth-callback
    redirect_uri = request.url_for(google_auth.__name__)
    print(f"redirect_uri {redirect_uri}")
    return await google_oauth_service.authorize_redirect(request, redirect_uri)


# @router.get("/set-session")
# def set_session(request: Request):
#     request.session["message"] = "Hello, World!"
#     return {"status": "session set"}
#
#
# @router.get("/get-session")
# def get_session(request: Request):
#     return {"session_value": request.session.get("message")}


class GetCurrentUserResponse(BaseModel):
    user: User


@router.get("/users/current")
async def get_current_user_response() -> GetCurrentUserResponse:
    user_token = session_data_provider.get_current_session().user_token
    with transaction() as session:
        db_user = session.query(DbUser).filter(DbUser.token == user_token).one()
        return GetCurrentUserResponse(user=db_user.to_model())


class UserSignupRequest(BaseModel):
    email_address: str


class UserSignupResponse(BaseModel):
    user: User


@router.get("/users/current")
async def get_current_user() -> UserSignupResponse:
    with transaction() as session:
        db_user = DbUser.create_user(session, email_address=request.email_address, role=UserRole.RESPONDENT)
        return UserSignupResponse(user=db_user.to_model())


@router.post("/users/signup")
async def user_signup(request: UserSignupRequest) -> UserSignupResponse:
    with transaction() as session:
        db_user = DbUser.create_user(session, email_address=request.email_address, role=UserRole.RESPONDENT)
        return UserSignupResponse(user=db_user.to_model())
