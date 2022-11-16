from __future__ import annotations
from __future__ import annotations

from typing import Dict, List

from sqlalchemy import ForeignKey, Column, Integer, Text
from sqlalchemy.orm import relationship

from database.connection import DbBase, Session
from database.db_entities.db_quiz import DbQuiz
from models.quiz_models import QuizFreeFormQuestion

EXCLUDE_PROFILES = {1, 27, 37, 44, 45, 46, 48}


class DbQuizFreeFormQuestion(DbBase):
    __tablename__ = 'quiz_free_form_questions'
    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    free_form_question = Column(Text)
    free_form_answer = Column(Text)

    quiz = relationship('DbQuiz', back_populates='quiz_free_form_questions', lazy='select')

    def to_model(self) -> QuizFreeFormQuestion:
        return QuizFreeFormQuestion(
            question=self.free_form_question,
            answer=self.free_form_answer,
        )

    @staticmethod
    def create_free_form_question(
            session: Session,
            db_quiz: DbQuiz,
            free_form_question: str,
            free_form_answer: str,
    ) -> DbQuizFreeFormQuestion:
        db_quiz_free_form_questions = DbQuizFreeFormQuestion(
            # SqlAlchemy won't immediately update the relationship fields, so we need to set it manually
            quiz_id=db_quiz.id,
            # quiz=db_quiz,
            free_form_question=free_form_question,
            free_form_answer=free_form_answer,
        )
        session.add(db_quiz_free_form_questions)
        return db_quiz_free_form_questions
