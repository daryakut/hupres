from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.connection import DbBase, Session
from database.db_entities.db_user import DbUser
from database.db_types.string_enum_db_type import StringEnumDbType
from database.db_types.token_db_type import TokenDbType
from models.token import Token
from models.sign import Sign
from models.quiz_models import Quiz
from models.pronounce import Pronounce


class DbQuiz(DbBase):
    __tablename__ = 'quizzes'
    id = Column(Integer, primary_key=True)
    token = Column(TokenDbType, unique=True)
    session_token = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))
    deleted_at = Column(DateTime)
    subject_name = Column(String(100))
    pronounce = Column(StringEnumDbType(Pronounce))
    dm_after_step_1 = Column(StringEnumDbType(Sign))
    dm_after_step_2 = Column(StringEnumDbType(Sign))
    dm_after_step_3 = Column(StringEnumDbType(Sign))
    dm_after_step_4 = Column(StringEnumDbType(Sign))

    user = relationship('DbUser', lazy='select')
    quiz_questions = relationship('DbQuizQuestion', back_populates='quiz', lazy='select')
    quiz_answers = relationship('DbQuizAnswer', back_populates='quiz', lazy='select')
    quiz_summaries = relationship('DbQuizSummary', back_populates='quiz', lazy='select')
    quiz_free_form_questions = relationship('DbQuizFreeFormQuestion', back_populates='quiz', lazy='select')

    def to_model(self) -> Quiz:
        return Quiz(
            token=self.token.value,
            user_token=self.user.token.value if self.user else None,
            subject_name=self.subject_name,
            pronounce=self.pronounce,
            dm_after_step_1=self.dm_after_step_1,
            dm_after_step_2=self.dm_after_step_2,
            dm_after_step_3=self.dm_after_step_3,
            dm_after_step_4=self.dm_after_step_4,
        )

    @staticmethod
    def create_quiz(session: Session, session_token: str, user_token: Optional[str]) -> DbQuiz:
        db_user = DbUser.find_by_token(session, user_token) if user_token else None
        db_quiz = DbQuiz(
            token=Token.generate_quiz_token(),
            session_token=session_token,
            user_id=db_user.id if db_user else None,
            # SqlAlchemy won't immediately update the db_user field, so we need to set it manually
            user=db_user,
        )
        session.add(db_quiz)
        return db_quiz
