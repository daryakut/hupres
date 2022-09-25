from __future__ import annotations

from quizzes.models import User
from quizzes.quizzes_api import CreateQuizResponse, create_quiz, get_quizzes, \
    GetQuizzesResponse
from tests.users.google_oauth import get_test_google_oauth_service
from tests.users.sessions import get_test_session_data_provider
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


class AnonymousUserTester:
    session_token: str

    def __init__(self, session_token: str):
        # This emulates first page visit when session is created. We test outside of scope of sessions,
        # so we need to do it manually
        self.session_token = session_token

    async def create_quiz(self) -> CreateQuizResponse:
        return await create_quiz()

    async def get_quizzes(self) -> GetQuizzesResponse:
        return await get_quizzes()

    @staticmethod
    async def visit():
        # Simulates a new anonymous user visiting the site
        return AnonymousUserTester(get_test_session_data_provider().initialize_session().session_token)


class UserTester(AnonymousUserTester):
    user: User

    def __init__(self, session_token: str, user: User):
        super().__init__(session_token)
        self.user = user

    @staticmethod
    # async def signup(email_address: str = "georgii@hupres.com") -> UserTester:
    async def login_with_google(email_address: str = "georgii@hupres.com"):
        session_token = get_test_session_data_provider().initialize_session().session_token

        get_test_google_oauth_service().email_address_to_return = email_address
        await google_auth(None)
        response = await get_current_user_response()
        return UserTester(session_token, response.user)
