from __future__ import annotations

from typing import List

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy import JSON
from sqlalchemy.orm import relationship

from database.common import DbBase, Session
from database.db_quiz import DbQuiz
from database.string_enum_db_type import StringEnumDbType
from models.token import Token
from quizzes.common import first_or_none
from quizzes.constants import QuizStep, QuizSubStep, Sign
from quizzes.question_database import QuestionName


class DbQuizQuestion(DbBase):
    __tablename__ = 'quiz_questions'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    # question_id = Column(Integer, ForeignKey('questions.id'))
    question_name = Column(StringEnumDbType(QuestionName))
    quiz_step = Column(StringEnumDbType(QuizStep))
    quiz_substep = Column(StringEnumDbType(QuizSubStep))
    followup_question_signs = Column(JSON)

    quiz = relationship('DbQuiz', back_populates='quiz_questions', lazy='select')
    # question = relationship('DbQuestion', lazy='select')

    # there should be max one answer per question, so we expose it via property
    _quiz_answers = relationship('DbQuizAnswer', back_populates='quiz_question', lazy='select')

    @property
    def answer(self) -> 'DbAnswer':
        quiz_answers = self._quiz_answers
        if len(quiz_answers) > 1:
            raise ValueError('QuizQuestion has more than one answer')
        return first_or_none(quiz_answers)

    @staticmethod
    def create_quiz_question(
            session: Session,
            db_quiz: DbQuiz,
            question_name: QuestionName,
            quiz_step: QuizStep,
            quiz_substep: QuizSubStep,
            followup_question_signs: List[Sign],
    ) -> DbQuizQuestion:
        db_quiz_question = DbQuizQuestion(
            token=Token.generate_quiz_question_token().value,
            # SqlAlchemy won't immediately update the relationship fields, so we need to set it manually
            quiz_id=db_quiz.id,
            quiz=db_quiz,

            question_name=question_name,
            quiz_step=quiz_step,
            quiz_substep=quiz_substep,
            followup_question_signs=followup_question_signs,
        )
        session.add(db_quiz_question)
        return db_quiz_question
