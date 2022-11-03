from __future__ import annotations

from typing import List, Union, Optional

from database.connection import Session
from database.db_entities.db_quiz import DbQuiz
from database.db_entities.db_quiz_answer import DbQuizAnswer
from database.db_entities.db_quiz_question import DbQuizQuestion
from models.token import Token
from common.utils import first_or_none
from quizzes.quiz_steps import QuizStep, TABLET_SUB_STEPS
from models.quiz_models import Quiz


class QuizAnswerQueries:

    @staticmethod
    def find_by_token(session: Session, token: Union[Token[Quiz], str]) -> DbQuizAnswer:
        token = token if isinstance(token, Token) else Token(value=token)
        return session.query(DbQuizAnswer).filter(DbQuizAnswer.token == token).one()

    @staticmethod
    def get_first_two_non_zero_tablet_answers(session: Session, quiz_token: Token[Quiz]) -> List[DbQuizAnswer]:
        return session.query(DbQuizAnswer) \
            .join(DbQuiz) \
            .join(DbQuizQuestion) \
            .filter(DbQuiz.token == quiz_token) \
            .filter(DbQuizQuestion.quiz_step == QuizStep.STEP_1) \
            .filter(DbQuizQuestion.quiz_substep.in_(TABLET_SUB_STEPS)) \
            .filter(DbQuizAnswer.is_all_zeros == False) \
            .distinct(DbQuizAnswer.id) \
            .order_by(DbQuizAnswer.id.asc()) \
            .limit(2) \
            .all()

    @staticmethod
    def find_last_for_quiz(session: Session, quiz_token: Token[Quiz]) -> Optional[DbQuizAnswer]:
        db_quiz_answers = session.query(DbQuizAnswer) \
            .join(DbQuiz) \
            .filter(DbQuiz.token == quiz_token) \
            .order_by(DbQuizAnswer.id.desc()) \
            .limit(1) \
            .all()
        return first_or_none(db_quiz_answers)
