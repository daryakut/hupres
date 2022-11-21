import re
from typing import Optional

from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import RedirectResponse

from common.env import FRONTEND_URL
from database.db_entities.db_user import DbUser
from database.queries.quiz_queries import QuizQueries
from database.transaction import transaction
from models.user import User
from models.user_role import UserRole
from users.google_oauth import GOOGLE_AUTH_CALLBACK_PATH, google_oauth_service, REDIRECT_URI
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
            role = db_user.role
            user_token = db_user.token
        else:
            raise Exception(f"Multiple users with email address {sanitized_email_address}")

        session_data = session_data_provider.get_current_session()
        db_quizzes_owned_by_session = QuizQueries.find_all_by_logged_out_session_token(
            session,
            session_token=session_data.session_token,
        )
        for db_quiz in db_quizzes_owned_by_session:
            print(f"Updating quiz ${db_quiz.token} owner to ${db_user.token}")
            db_quiz.user_id = db_user.id

    session_data_provider.update_current_session(user_token=user_token, user_role=role)
    # return {"email": email_address, "user_token": user_token.value}
    return RedirectResponse(url=FRONTEND_URL)


@router.get("/api/users/google-login")
async def google_login(request: Request):
    print(f"redirect_uri {REDIRECT_URI}")
    return await google_oauth_service.authorize_redirect(request, REDIRECT_URI)


class GetCurrentUserResponse(BaseModel):
    """Missing user means user is not logged in"""
    user: Optional[User]


@router.get("/api/users/current")
async def get_current_user() -> GetCurrentUserResponse:
    # user_token = Token(session_data_provider.get_current_session().user_token)
    user_token = session_data_provider.get_current_session().user_token
    if user_token is None:
        # User is not logged in
        return GetCurrentUserResponse(user=None)

    with transaction() as session:
        db_users = session.query(DbUser).filter(DbUser.token == user_token).all()
        if len(db_users) == 0:
            # User not found, let's sign out. This is for cases when user is deleted from the database
            # Should not be happening, but this is a temporary measure during release when we nuke the prod DB
            # We logout the user so that they can login again with new user
            session_data_provider.update_current_session(user_token=None, user_role=None)
            return GetCurrentUserResponse(user=None)

        assert len(db_users) == 1
        return GetCurrentUserResponse(user=db_users[0].to_model())


@router.get("/api/users/logout")
async def logout():
    session_data_provider.update_current_session(user_token=None, user_role=None)
