from __future__ import annotations

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy import JSON
from sqlalchemy.orm import relationship, backref

from database.common import DbBase
from quizzes.models import Answer


class DbAnswer(DbBase):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer_name = Column(String(100))
    sign_scores = Column(JSON)

    # question = relationship('DbQuestion', backref=backref('answers', lazy=True))

    def to_model(self) -> Answer:
        return Answer(
            token=self.token,
            question_token=self.question.token,
            answer_name=self.answer_name,
            sign_scores=self.sign_scores
        )
