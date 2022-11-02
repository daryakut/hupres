from __future__ import annotations

from typing import List, Union

from database.connection import Session
from database.db_entities.db_quiz import DbQuiz
from database.db_entities.db_user import DbUser
from models.token import Token
from quizzes.models import Quiz, User


class QuizQueries:

    @staticmethod
    def find_by_token(session: Session, token: Union[Token[Quiz], str]) -> DbQuiz:
        token = token if isinstance(token, Token) else Token(value=token)
        return session.query(DbQuiz).filter(DbQuiz.token == token).one()

    @staticmethod
    def find_all_by_logged_out_session_token(session: Session, session_token: str) -> List[DbQuiz]:
        return session.query(DbQuiz) \
            .filter(DbQuiz.session_token == session_token) \
            .filter(DbQuiz.user_id == None) \
            .filter(DbQuiz.deleted_at == None) \
            .all()

    @staticmethod
    def find_all_by_user_token(session: Session, user_token: Union[Token[User], str]) -> List[DbQuiz]:
        user_token = user_token if isinstance(user_token, Token) else Token(value=user_token)
        return session.query(DbQuiz) \
            .join(DbUser) \
            .filter(DbUser.token == user_token) \
            .filter(DbQuiz.deleted_at == None) \
            .all()
