from __future__ import annotations

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy import JSON
from sqlalchemy.orm import relationship

from database.common import DbBase
from quizzes.common import first_or_none


class DbQuizQuestion(DbBase):
    __tablename__ = 'quiz_questions'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    # question_id = Column(Integer, ForeignKey('questions.id'))
    question_name = Column(String(50))
    : UserRole = Column(IntEnumDbType(QuizStep), nullable=False)
    quiz_step = Column(Integer)
    quiz_substep = Column(Integer)
    followup_question_signs = Column(JSON)

    # quiz = relationship('DbQuiz', back_populates='questions', lazy='select')
    # question = relationship('DbQuestion', lazy='select')
    #
    # # there should be max one answer per question, so we expose it via property
    # __quiz_answers = relationship('DbQuizAnswer', back_populates='quiz_question', lazy='select')

    @property
    def answer(self) -> 'DbAnswer':
        quiz_answers = self.__quiz_answers
        if len(quiz_answers) > 1:
            raise ValueError('QuizQuestion has more than one answer')
        return first_or_none(quiz_answers)
