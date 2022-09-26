from __future__ import annotations

from typing import List, Union

from database.common import Session
from database.db_quiz import DbQuiz
from database.db_user import DbUser
from models.token import Token
from quizzes.models import Quiz


class QuizQueries:

    @staticmethod
    def find_by_token(session: Session, token: Union[Token[Quiz], str]) -> DbQuiz:
        token = token.value if isinstance(token, Token) else token
        return session.query(DbQuiz).filter(DbQuiz.token == token).one()

    @staticmethod
    def find_all_by_logged_out_session_token(session: Session, session_token: str) -> List[DbQuiz]:
        return session.query(DbQuiz) \
            .filter(DbQuiz.session_token == session_token) \
            .filter(DbQuiz.user_id == None) \
            .filter(DbQuiz.deleted_at == None) \
            .all()

    @staticmethod
    def find_all_by_user_token(session: Session, user_token: str) -> List[DbQuiz]:
        return session.query(DbQuiz) \
            .join(DbUser) \
            .filter(DbUser.token == user_token) \
            .filter(DbQuiz.deleted_at == None) \
            .all()
