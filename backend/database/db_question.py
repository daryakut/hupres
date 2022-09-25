from __future__ import annotations

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database.common import DbBase
from quizzes.models import Question


class DbQuestion(DbBase):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    question_name = Column(String(100))
    is_tablet = Column(Boolean)

    # answers = relationship('DbAnswer', back_populates='question', lazy='select')

    def to_model(self) -> Question:
        return Question(
            token=self.token,
            question_name=self.question_name,
            is_tablet=self.is_tablet
        )
