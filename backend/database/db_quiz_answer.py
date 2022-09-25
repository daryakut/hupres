from __future__ import annotations

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy import JSON
from sqlalchemy.orm import relationship

from database.common import DbBase


class DbQuizAnswer(DbBase):
    __tablename__ = 'quiz_answers'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    quiz_question_id = Column(Integer, ForeignKey('quiz_questions.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))
    current_sign_scores = Column(JSON)
    original_sign_scores = Column(JSON)

    # quiz = relationship('DbQuiz', back_populates='questions', lazy='select')
    # quiz_question = relationship('DbQuizQuestion', back_populates='__quiz_answers', lazy='select')
    # answer = relationship('DbAnswer', lazy='select')
