from __future__ import annotations

import json
from typing import List

from pydantic import BaseModel

from common.utils import check, check_not_none
from database.db_entities.db_quiz_question import DbQuizQuestion
from database.db_entities.db_quiz_summary import DbQuizSummary
from database.queries.quiz_answer_queries import QuizAnswerQueries
from database.queries.quiz_queries import QuizQueries
from database.transaction import transaction
from models.pronounce import Pronounce
from models.quiz_models import Quiz, QuizSummary
from models.token import Token
from quizzes.charts import get_chart_info, Gender, export_chart_info
from quizzes.quiz_steps import QuizStep, QuizSubStep




PRODUCT_ID = 11
EXCLUDE_PROFILES = {1, 27, 37, 44, 45, 46, 48}


def api_generate_quiz_summary(quiz_token: Token[Quiz]) -> QuizSummary:
    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, quiz_token)

        db_last_answer = QuizAnswerQueries.find_last_for_quiz(session, quiz_token)
        check_not_none(db_last_answer, "Cannot find last answer for quiz")

        db_last_question: DbQuizQuestion = db_last_answer.quiz_question
        check(
            lambda: db_last_question.quiz_step == QuizStep.STEP_6 and
                    db_last_question.quiz_substep == QuizSubStep.STEP6_SUBSTEP_10_20_30,
            "Quiz is not finished yet, cannot generate the summary"
        )

        last_sign_scores = db_last_answer.current_sign_scores
        respondent_name = db_quiz.subject_name
        respondent_pronounce = db_quiz.pronounce

    if respondent_pronounce == Pronounce.SHE_HER:
        gender = Gender.FEMALE
    elif respondent_pronounce == Pronounce.HE_HIM:
        gender = Gender.MALE
    else:
        gender = Gender.NONE

    chart_info = get_chart_info(
        product_id=PRODUCT_ID,
        soma_type=last_sign_scores,
        respondent_name=respondent_name,
        gender=gender,
    )
    chart_summary = export_chart_info(chart_info)

    # Doing this in a separate transaction to keep them short
    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, quiz_token)
        db_quiz_summary = DbQuizSummary.create_quiz_summary(
            session=session,
            db_quiz=db_quiz,
            chart_summary=chart_summary,
        )
        return db_quiz_summary.to_model()
