from __future__ import annotations

from typing import Optional, List

from database.queries.quiz_answer_queries import QuizAnswerQueries
from database.queries.quiz_queries import QuizQueries
from database.queries.quiz_question_queries import QuizQuestionQueries
from database.transaction import transaction
from models.pronounce import Pronounce
from models.quiz_models import QuizQuestion, AvailableAnswer, Quiz
from models.sign import Sign
from models.token import Token
from models.user import User
from quizzes.question_database import QuestionName
from quizzes.quiz_steps import QuizStep, QuizSubStep
from quizzes.quiz_summary import GenerateQuizSummaryResponse
from quizzes.quizzes_api import CreateQuizResponse, create_quiz, get_quizzes, \
    GetQuizzesResponse, delete_quiz, get_next_quiz_question, submit_quiz_answer, SubmitQuizAnswerRequest, \
    generate_quiz_summary, UpdateQuizRequest, update_quiz
from tests.users.fake_google_oauth import get_fake_google_oauth_service
from tests.users.fake_sessions import get_fake_session_data_provider
from users.users_api import google_auth, get_current_user_response, ADMIN_USER_EMAIL_ADDRESSES, logout


# client = TestClient(app)
#
# def test_read_item():
#     item_id = 1
#     response = client.get(f"/items/{item_id}")
#
#     assert response.status_code == 200
#     assert response.json() == {"item_id": 1, "name": "Item Name"}


class QuizTester:
    quiz: Quiz

    def __init__(self, quiz: Quiz):
        self.quiz = quiz

    def refresh_from_db(self):
        with transaction() as session:
            db_quiz = QuizQueries.find_by_token(session, self.quiz.token)
            self.quiz = db_quiz.to_model()


class QuizQuestionTester:
    quiz_token: str
    quiz_question: QuizQuestion
    available_answers: List[AvailableAnswer]
    question_name: QuestionName
    quiz_step: QuizStep
    quiz_substep: QuizSubStep
    followup_question_signs: List[Sign]
    answer_token: Optional[Token[AvailableAnswer]]

    def __init__(self, quiz_token: str, quiz_question: Optional[QuizQuestion],
                 available_answers: List[AvailableAnswer]):
        self.quiz_token = quiz_token
        self.quiz_question = quiz_question
        self.available_answers = available_answers
        if quiz_question:
            assert quiz_question.token.startswith("qq_")
            self.refresh_from_db()

    def refresh_from_db(self):
        with transaction() as session:
            db_question = QuizQuestionQueries.find_by_token(session, self.quiz_question.token)
            assert db_question.quiz.token.value == self.quiz_token
            assert db_question.token.value == self.quiz_question.token
            self.question_name = db_question.question_name
            self.quiz_step = db_question.quiz_step
            self.quiz_substep = db_question.quiz_substep
            self.followup_question_signs = db_question.followup_question_signs
            self.answer_token = db_question.answer.token.value if db_question.answer is not None else None


class QuizAnswerTester:
    quiz_question_token: str
    quiz_answer_token: str
    quiz_token: str
    answer_name: str
    is_all_zeros: bool
    current_sign_scores: List[int]
    original_sign_scores: List[int]
    signs_for_next_questions: List[Sign]

    def __init__(self, quiz_question_token: str, quiz_answer_token: str):
        assert quiz_answer_token.startswith("qa_")
        self.quiz_question_token = quiz_question_token
        self.quiz_answer_token = quiz_answer_token
        self.refresh_from_db()

    def refresh_from_db(self):
        with transaction() as session:
            db_answer = QuizAnswerQueries.find_by_token(session, self.quiz_answer_token)
            assert db_answer.quiz_question.token.value == self.quiz_question_token
            assert db_answer.token.value == self.quiz_answer_token

            self.quiz_token = db_answer.quiz.token.value
            self.answer_name = db_answer.answer_name
            self.is_all_zeros = db_answer.is_all_zeros
            self.current_sign_scores = db_answer.current_sign_scores
            self.original_sign_scores = db_answer.original_sign_scores
            self.signs_for_next_questions = db_answer.signs_for_next_questions


class UserTester:
    session_token: str
    user: User

    def __init__(self, session_token: str, user: Optional[User] = None):
        self.session_token = session_token
        self.user = user

    async def create_quiz(self) -> QuizTester:
        response = await create_quiz()
        return QuizTester(quiz=response.quiz)

    async def update_quiz(self, quiz_token: str, subject_name: str, pronounce: Pronounce):
        await update_quiz(quiz_token, UpdateQuizRequest(subject_name=subject_name, pronounce=pronounce))

    async def get_quizzes(self) -> GetQuizzesResponse:
        return await get_quizzes()

    async def delete_quiz(self, quiz_token: str) -> CreateQuizResponse:
        return await delete_quiz(quiz_token)

    async def get_next_quiz_question(self, quiz_token: str) -> QuizQuestionTester:
        response = await get_next_quiz_question(quiz_token)
        return QuizQuestionTester(
            quiz_token=quiz_token,
            quiz_question=response.quiz_question,
            available_answers=response.available_answers,
        )

    async def submit_quiz_answer(self, quiz_question_token: str, answer_name: str) -> QuizAnswerTester:
        response = await submit_quiz_answer(quiz_question_token, SubmitQuizAnswerRequest(answer_name=answer_name))
        return QuizAnswerTester(quiz_question_token=quiz_question_token, quiz_answer_token=response.quiz_answer.token)

    async def generate_quiz_summary(self, quiz_token: str) -> GenerateQuizSummaryResponse:
        return await generate_quiz_summary(quiz_token)

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
