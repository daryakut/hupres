from __future__ import annotations

from typing import Optional

from quizzes.models import User
from quizzes.quizzes_api import CreateQuizResponse, create_quiz, get_quizzes, \
    GetQuizzesResponse, delete_quiz
from tests.users.fake_google_oauth import get_test_google_oauth_service
from tests.users.fake_sessions import get_test_session_data_provider
from users.session_data import SessionData
from users.users_api import google_auth, get_current_user_response


# client = TestClient(app)
#
# def test_read_item():
#     item_id = 1
#     response = client.get(f"/items/{item_id}")
#
#     assert response.status_code == 200
#     assert response.json() == {"item_id": 1, "name": "Item Name"}


class UserTester:
    session_token: str
    user: User

    def __init__(self, session_token: str, user: Optional[User] = None):
        self.session_token = session_token
        self.user = user

    async def create_quiz(self) -> CreateQuizResponse:
        return await create_quiz()

    async def get_quizzes(self) -> GetQuizzesResponse:
        return await get_quizzes()

    async def delete_quiz(self, quiz_token: str) -> CreateQuizResponse:
        return await delete_quiz(quiz_token)

    def is_logged_in(self) -> bool:
        return self.user is not None

    async def login_with_google(self, email_address: str = "georgii@hupres.com"):
        get_test_google_oauth_service().email_address_to_return = email_address
        await google_auth(None)
        response = await get_current_user_response()
        self.user = response.user

    @staticmethod
    async def visit():
        # Simulates a new anonymous user visiting the site
        return UserTester(get_test_session_data_provider().initialize_session().session_token)

    @staticmethod
    async def signup_with_google(email_address: str = "georgii@hupres.com"):
        user_tester = await UserTester.visit()
        await user_tester.login_with_google(email_address)
        return user_tester
