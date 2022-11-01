from __future__ import annotations

from typing import List, Union, Optional

from database.common import Session
from database.db_quiz import DbQuizAnswer, DbQuiz
from database.db_quiz_answer import DbQuizAnswer
from database.db_quiz_question import DbQuizQuestion
from models.token import Token
from quizzes.common import first_or_none
from quizzes.constants import QuizStep
from quizzes.models import Quiz


class QuizAnswerQueries:

    @staticmethod
    def find_by_token(session: Session, token: Union[Token[Quiz], str]) -> DbQuizAnswer:
        token = token.value if isinstance(token, Token) else token
        return session.query(DbQuizAnswer).filter(DbQuizAnswer.token == token).one()

    @staticmethod
    def get_first_two_non_zero_tablet_answers(session: Session, quiz_token: Token[Quiz]) -> List[DbQuizAnswer]:
        return session.query(DbQuizAnswer) \
            .join(DbQuiz) \
            .join(DbQuizQuestion) \
            .filter(DbQuiz.token == quiz_token) \
            .filter(DbQuizQuestion.quiz_step <= QuizStep.STEP_4.value) \
            .filter(DbQuizAnswer.is_all_zeros == True) \
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
