from __future__ import annotations

from gettext import gettext as _
from typing import Tuple, List, Optional

import numpy as np
from pydantic import BaseModel

from common.exceptions import Unauthorized, BadRequest
from common.utils import check
from database.connection import Session
from database.db_entities.db_quiz import DbQuiz
from database.db_entities.db_quiz_answer import DbQuizAnswer
from database.db_entities.db_quiz_question import DbQuizQuestion
from database.queries.quiz_answer_queries import QuizAnswerQueries
from database.queries.quiz_queries import QuizQueries
from database.queries.quiz_question_queries import QuizQuestionQueries
from database.transaction import transaction
from models.quiz_models import QuizQuestion, AvailableAnswer, Quiz, QuizAnswer
from models.sign import Sign
from models.token import Token
from quizzes.quiz_steps import QuizStep, QuizSubStep
from quizzes.question_database import QUESTION_NAMES_FOR_SIGNS, ANSWER_SCORES, QuestionName
from users.sessions import session_data_provider


def ask_free_form_question(quiz_token: Token[Quiz], question: str) -> str:
    session_data = session_data_provider.get_current_session()
    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, token=quiz_token)
        if db_quiz.deleted_at is not None:
            raise BadRequest(f"Cannot find quiz {quiz_token}")

        if not session_data.is_owner_of(db_quiz):
            raise Unauthorized("You are not allowed to access quiz")

        db_quiz.subject_name = request.subject_name
        db_quiz.pronounce = request.pronounce
