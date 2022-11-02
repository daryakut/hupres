from __future__ import annotations

from typing import Union

from database.connection import Session
from database.db_entities.db_quiz_question import DbQuizQuestion
from models.token import Token
from quizzes.models import QuizQuestion


class QuizQuestionQueries:

    @staticmethod
    def find_by_token(session: Session, token: Union[Token[QuizQuestion], str]) -> DbQuizQuestion:
        token = token if isinstance(token, Token) else Token(value=token)
        return session.query(DbQuizQuestion).filter(DbQuizQuestion.token == token).one()
