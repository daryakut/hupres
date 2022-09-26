from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from database.db_quiz import DbQuiz
from database.quiz_queries import QuizQueries
from database.transaction import transaction
from quizzes.models import Quiz
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


# class GetNextQuizQuestionResponse(BaseModel):
#     quiz_question: QuizQuestion
#     available_answers: List[Answer]
#
#
# @router.post("/quizzes/{quiz_token}/get-next-question")
# async def get_next_quiz_question() -> GetNextQuizQuestionResponse:
#     return CreateQuizResponse(quiz=Quiz())
