from __future__ import annotations

from typing import Optional

from quizzes.algorithm import GetNextQuizQuestionResponse, SubmitAnswerResponse
from quizzes.models import User
from quizzes.quizzes_api import CreateQuizResponse, create_quiz, get_quizzes, \
    GetQuizzesResponse, delete_quiz, get_next_quiz_question, submit_quiz_answer, SubmitQuizAnswerRequest
from tests.users.fake_google_oauth import get_fake_google_oauth_service
from tests.users.fake_sessions import get_fake_session_data_provider
from users.session_data import SessionData
from users.users_api import google_auth, get_current_user_response, ADMIN_USER_EMAIL_ADDRESSES, logout


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

    async def get_next_quiz_question(self, quiz_token: str) -> GetNextQuizQuestionResponse:
        return await get_next_quiz_question(quiz_token)

    async def submit_quiz_answer(self, quiz_question_token: str, answer_name: str) -> str:
        response = await submit_quiz_answer(quiz_question_token, SubmitQuizAnswerRequest(answer_name=answer_name))
        return response.quiz_answer_token

    def is_logged_in(self) -> bool:
        return self.user is not None

    async def login_with_google(self, email_address: str = "georgii@hupres.com"):
        get_fake_google_oauth_service().email_address_to_return = email_address
        await google_auth(None)
        response = await get_current_user_response()
        self.user = response.user

    async def logout(self):
        await logout()

    @staticmethod
    async def visit():
        # Simulates a new anonymous user visiting the site
        return UserTester(get_fake_session_data_provider().initialize_session().session_token)

    @staticmethod
    async def signup_with_google(email_address: str = "georgii@hupres.com"):
        user_tester = await UserTester.visit()
        await user_tester.login_with_google(email_address)
        return user_tester

    @staticmethod
    async def signup_admin():
        user_tester = await UserTester.visit()
        await user_tester.login_with_google(email_address=ADMIN_USER_EMAIL_ADDRESSES[0])
        return user_tester
