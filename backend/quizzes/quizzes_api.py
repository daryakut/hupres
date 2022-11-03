from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from common.clock import clock
from common.exceptions import Unauthorized, BadRequest
from database.db_entities.db_quiz import DbQuiz
from database.queries.quiz_queries import QuizQueries
from database.transaction import transaction
from models.pronounce import Pronounce
from models.quiz_models import Quiz
from models.token import Token
from quizzes.quiz_algorithm import api_get_next_question, GetNextQuizQuestionResponse, api_submit_answer, \
    SubmitAnswerResponse
from quizzes.quiz_summary import api_generate_quiz_summary, GenerateQuizSummaryResponse
from users.sessions import session_data_provider

router = APIRouter()


class CreateQuizResponse(BaseModel):
    quiz: Quiz


@router.post("/quizzes")
async def create_quiz() -> CreateQuizResponse:
    session_data = session_data_provider.get_current_session()
    with transaction() as session:
        db_quiz = DbQuiz.create_quiz(
            session,
            session_token=session_data.session_token,
            user_token=session_data.user_token,
        )
        quiz = db_quiz.to_model()

    return CreateQuizResponse(quiz=quiz)


class GetQuizzesResponse(BaseModel):
    quizzes: List[Quiz]


@router.get("/quizzes")
async def get_quizzes() -> GetQuizzesResponse:
    session_data = session_data_provider.get_current_session()
    with transaction() as session:
        if session_data.user_token is not None:
            db_quizzes = QuizQueries.find_all_by_user_token(
                session,
                user_token=session_data.user_token,
            )
        else:
            db_quizzes = QuizQueries.find_all_by_logged_out_session_token(
                session,
                session_token=session_data.session_token,
            )
        quizzes = [db_quiz.to_model() for db_quiz in db_quizzes]

    return GetQuizzesResponse(quizzes=quizzes)


@router.delete("/quizzes/{quiz_token}")
async def delete_quiz(quiz_token: str):
    session_data = session_data_provider.get_current_session()
    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, token=quiz_token)
        if db_quiz.deleted_at is not None:
            raise BadRequest(f"Cannot find quiz {quiz_token}")

        if not session_data.is_owner_of(db_quiz):
            raise Unauthorized("You are not allowed to delete this quiz")
        db_quiz.deleted_at = clock.now()


class UpdateQuizRequest(BaseModel):
    subject_name: str
    pronounce: Pronounce


@router.post("/quizzes/{quiz_token}")
async def update_quiz(quiz_token: str, request: UpdateQuizRequest):
    session_data = session_data_provider.get_current_session()
    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, token=quiz_token)
        if db_quiz.deleted_at is not None:
            raise BadRequest(f"Cannot find quiz {quiz_token}")

        if not session_data.is_owner_of(db_quiz):
            raise Unauthorized("You are not allowed to delete this quiz")

        db_quiz.subject_name = request.subject_name
        db_quiz.pronounce = request.pronounce


@router.post("/quizzes/{quiz_token}/generate-next-question")
async def get_next_quiz_question(quiz_token: str) -> GetNextQuizQuestionResponse:
    return api_get_next_question(Token.of(quiz_token))


class SubmitQuizAnswerRequest(BaseModel):
    answer_name: str


@router.post("/quiz-questions/{quiz_question_token}/submit-answer")
async def submit_quiz_answer(
        quiz_question_token: str,
        request: SubmitQuizAnswerRequest,
) -> SubmitAnswerResponse:
    # TODO: check access rights
    return api_submit_answer(Token.of(quiz_question_token), request.answer_name)


@router.post("/quizzes/{quiz_token}/generate-summary")
async def generate_quiz_summary(quiz_token: str) -> GenerateQuizSummaryResponse:
    return api_generate_quiz_summary(Token.of(quiz_token))
