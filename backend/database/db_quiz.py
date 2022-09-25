from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

from database.common import DbBase, Session
from database.db_user import DbUser
from models.token import Token
from quizzes.constants import Sign
from quizzes.models import Pronounce, Quiz


class DbQuiz(DbBase):
    __tablename__ = 'quizzes'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    session_token = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))
    subject_name = Column(String(100))
    pronounce = Column(String(50))
    dm_after_step_1 = Column(String(10))
    dm_after_step_2 = Column(String(10))
    dm_after_step_3 = Column(String(10))
    dm_after_step_4 = Column(String(10))

    user = relationship('DbUser', lazy='select')
    # quiz_questions = relationship('DbQuizQuestion', back_populates='quiz', lazy='select')
    # quiz_answers = relationship('DbQuizAnswer', back_populates='quiz', lazy='select')

    def to_model(self) -> Quiz:
        return Quiz(
            token=self.token,
            user_token=self.user.token if self.user else None,
            subject_name=self.subject_name,
            pronounce=Pronounce(self.pronounce) if self.pronounce else None,
            dm_after_step_1=Sign(self.dm_after_step_1) if self.dm_after_step_1 else None,
            dm_after_step_2=Sign(self.dm_after_step_2) if self.dm_after_step_2 else None,
            dm_after_step_3=Sign(self.dm_after_step_3) if self.dm_after_step_3 else None,
            dm_after_step_4=Sign(self.dm_after_step_4) if self.dm_after_step_4 else None,
        )

    @staticmethod
    def create_quiz(session: Session, session_token: str, user_token: Optional[str]) -> DbQuiz:
        user_id = DbUser.find_by_token(session, user_token).id if user_token else None
        db_quiz = DbQuiz(
            token=Token.generate_quiz_token().value,
            session_token=session_token,
            user_id=user_id,
        )
        session.add(db_quiz)
        return db_quiz
