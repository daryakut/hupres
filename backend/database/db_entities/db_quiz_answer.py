from __future__ import annotations
from __future__ import annotations

from typing import List

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy import JSON
from sqlalchemy.orm import relationship

from database.db_entities.db_timestamped_entity import DbTimestampedEntity
from database.db_types.json_enum_list_db_type import JsonEnumListDbType
from models.quiz_models import QuizAnswer
from database.connection import DbBase, Session
from database.db_entities.db_quiz import DbQuiz
from database.db_entities.db_quiz_question import DbQuizQuestion
from database.db_types.token_db_type import TokenDbType
from models.token import Token
from models.sign import Sign


class DbQuizAnswer(DbTimestampedEntity, DbBase):
    __tablename__ = 'quiz_answers'
    id = Column(Integer, primary_key=True)
    token = Column(TokenDbType, unique=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    quiz_question_id = Column(Integer, ForeignKey('quiz_questions.id'))
    answer_names = Column(JSON)
    is_all_zeros = Column(Boolean)

    # A list of signs, for which we should be asking questions, *including* this answer's question
    # We need to keep track of this question for is_all_zero answers, for which we should ask next question
    # for the same sign as previous one
    # TODO: we probably don't need this as it's the same as followup_question_signs
    current_sign_scores = Column(JSON)

    # TODO: deprecated, remove
    original_sign_scores = Column(JSON)
    signs_for_next_questions = Column(JsonEnumListDbType(Sign))

    quiz = relationship('DbQuiz', back_populates='quiz_answers', lazy='select')
    quiz_question = relationship('DbQuizQuestion', back_populates='_quiz_answers', lazy='select')

    def to_model(self) -> QuizAnswer:
        return QuizAnswer(
            token=self.token.value,
        )

    @staticmethod
    def create_quiz_answer(
            session: Session,
            db_quiz: DbQuiz,
            db_quiz_question: DbQuizQuestion,
            answer_names: List[str],
            is_all_zeros: bool,
            current_sign_scores: List[int],
            signs_for_next_questions: List[Sign],
    ) -> DbQuizAnswer:
        db_quiz_answer = DbQuizAnswer(
            token=Token.generate_quiz_answer_token(),
            # SqlAlchemy won't immediately update the relationship fields, so we need to set it manually
            quiz_id=db_quiz.id,
            quiz=db_quiz,
            quiz_question_id=db_quiz_question.id,
            quiz_question=db_quiz_question,

            answer_names=answer_names,
            is_all_zeros=is_all_zeros,
            current_sign_scores=current_sign_scores,
            original_sign_scores=[],
            signs_for_next_questions=signs_for_next_questions,
        )
        session.add(db_quiz_answer)
        return db_quiz_answer
