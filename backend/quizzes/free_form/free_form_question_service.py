from __future__ import annotations

from common.exceptions import Unauthorized, BadRequest
from database.db_entities.db_quiz_free_form_question import DbQuizFreeFormQuestion
from database.queries.quiz_queries import QuizQueries
from database.transaction import transaction
from models.quiz_models import Quiz, QuizSummary
from models.token import Token
from quizzes.free_form.gpt_client import ask_gpt
from users.sessions import session_data_provider


def api_ask_free_form_question(quiz_token: Token[Quiz], free_form_question: str) -> str:
    session_data = session_data_provider.get_current_session()
    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, token=quiz_token)
        if db_quiz.deleted_at is not None:
            raise BadRequest(f"Cannot find quiz {quiz_token}")

        if not session_data.is_owner_of(db_quiz):
            raise Unauthorized("You are not allowed to access quiz")

        respondent_name = db_quiz.subject_name
        pronounce = db_quiz.pronounce

        quiz_summaries = db_quiz.quiz_summaries
        if not len(quiz_summaries):
            raise BadRequest("Quiz is not complete yet")

        db_last_summary = quiz_summaries[-1]
        summary: QuizSummary = db_last_summary.to_model()

    text_summary = "\n\n".join([f"{s.title}: {s.summary}" for s in summary.summaries])
    print("Text summary", text_summary)
    print("Asking question", free_form_question)
    free_form_answer = ask_gpt(
        respondent_summary=text_summary,
        free_form_question=free_form_question,
        respondent_name=respondent_name,
        pronounce=pronounce,
    )
    print("GPT responded", free_form_answer)

    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, token=quiz_token)
        DbQuizFreeFormQuestion.create_free_form_question(
            session=session,
            db_quiz=db_quiz,
            free_form_question=free_form_question,
            free_form_answer=free_form_answer,
        )

    return free_form_answer
