from __future__ import annotations

from typing import List

from database.common import Session
from database.db_quiz import DbQuiz
from database.db_user import DbUser


class QuizQueries:

    @staticmethod
    def find_all_by_logged_out_session_token(session: Session, session_token: str) -> List[DbQuiz]:
        return session.query(DbQuiz) \
            .filter(DbQuiz.session_token == session_token) \
            .filter(DbQuiz.user_id == None) \
            .all()

    @staticmethod
    def find_all_by_user_token(session: Session, user_token: str) -> List[DbQuiz]:
        return session.query(DbQuiz) \
            .join(DbUser) \
            .filter(DbUser.token == user_token) \
            .all()


def find_all_by_session_token(session: Session, session_token: str) -> List[DbQuiz]:
    return session.query(DbQuiz) \
        .filter(DbQuiz.session_token == session_token) \
        .all()
