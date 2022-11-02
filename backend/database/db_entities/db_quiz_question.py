from __future__ import annotations

from typing import List

from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy import JSON
from sqlalchemy.orm import relationship

from database.connection import DbBase, Session
from database.db_entities.db_quiz import DbQuiz
from database.db_types.string_enum_db_type import StringEnumDbType
from database.db_types.token_db_type import TokenDbType
from models.quiz_models import QuizQuestion
from models.token import Token
from common.utils import first_or_none
from quizzes.quiz_steps import QuizStep, QuizSubStep
from models.sign import Sign
from quizzes.question_database import QuestionName
from gettext import gettext as _


class DbQuizQuestion(DbBase):
    __tablename__ = 'quiz_questions'
    id = Column(Integer, primary_key=True)
    token = Column(TokenDbType, unique=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    question_name = Column(StringEnumDbType(QuestionName))
    quiz_step = Column(StringEnumDbType(QuizStep))
    quiz_substep = Column(StringEnumDbType(QuizSubStep))
    followup_question_signs = Column(JSON)

    quiz = relationship('DbQuiz', back_populates='quiz_questions', lazy='select')

    # there should be max one answer per question, so we expose it via property
    _quiz_answers = relationship('DbQuizAnswer', back_populates='quiz_question', lazy='select')

    @property
    def answer(self) -> 'DbAnswer':
        quiz_answers = self._quiz_answers
        if len(quiz_answers) > 1:
            raise ValueError('QuizQuestion has more than one answer')
        return first_or_none(quiz_answers)

    def to_model(self) -> QuizQuestion:
        return QuizQuestion(
            token=self.token.value,
            question_name=self.question_name,
            question_display_name=_(self.question_name.value),
        )

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
            token=Token.generate_quiz_question_token(),
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
