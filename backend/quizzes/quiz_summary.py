from __future__ import annotations

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
from quizzes.charts.charts import NAME_PLACEHOLDER
from quizzes.quiz_steps import QuizStep, QuizSubStep

# This product ID does not exist. Whatever we put here will be excluded from the result, so let's not have anything real
PRODUCT_ID = 11
EXCLUDE_PROFILES = {1, 27, 37, 44, 45, 46, 48}


def api_generate_quiz_summary(quiz_token: Token[Quiz]) -> QuizSummary:
    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, quiz_token)
        quiz_summaries = db_quiz.quiz_summaries
        if len(quiz_summaries):
            return quiz_summaries[-1].to_model_book_profile()

        db_last_answer = QuizAnswerQueries.find_last_for_quiz(session, quiz_token)
        check_not_none(db_last_answer, "Cannot find last answer for quiz")

        db_last_question: DbQuizQuestion = db_last_answer.quiz_question
        # TODO: fix this so that it works when no questions are left for a sign
        if (db_last_question.quiz_step != QuizStep.STEP_6
                or db_last_question.quiz_substep != QuizSubStep.STEP6_SUBSTEP_10_20_30):
            print("WARN: Quiz is not finished yet, perhaps there were no questions available for sign")
        # check(
        #     lambda: db_last_question.quiz_step == QuizStep.STEP_6 and
        #             db_last_question.quiz_substep == QuizSubStep.STEP6_SUBSTEP_10_20_30,
        #     "Quiz is not finished yet, cannot generate the summary"
        # )

        last_sign_scores = db_last_answer.current_sign_scores
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
        respondent_name=NAME_PLACEHOLDER,  # We want to have ZZZ in the original texts to be able to translate them
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
        return db_quiz_summary.to_model_book_profile()
