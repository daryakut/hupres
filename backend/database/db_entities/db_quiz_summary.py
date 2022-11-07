# from __future__ import annotations
# from __future__ import annotations
#
# from typing import List, Dict
#
# from sqlalchemy import Boolean
# from sqlalchemy import ForeignKey, Column, Integer, String
# from sqlalchemy import JSON
# from sqlalchemy.orm import relationship
#
# from database.db_types.json_enum_list_db_type import JsonEnumListDbType
# from models.quiz_models import QuizAnswer
# from database.connection import DbBase, Session
# from database.db_entities.db_quiz import DbQuiz
# from database.db_entities.db_quiz_question import DbQuizQuestion
# from database.db_types.token_db_type import TokenDbType
# from models.token import Token
# from models.sign import Sign
#
#
# class DbQuizSummary(DbBase):
#     __tablename__ = 'quiz_summaries'
#     id = Column(Integer, primary_key=True)
#     quiz_id = Column(Integer, ForeignKey('quizzes.id'))
#     chart_summary = Column(JSON)
#
#     quiz = relationship('DbQuiz', back_populates='quiz_summaries', lazy='select')
#
#     def to_model(self) -> QuizAnswer:
#         return QuizAnswer(
#             token=self.token.value,
#         )
#
#     @staticmethod
#     def create_quiz_summary(
#             session: Session,
#             db_quiz: DbQuiz,
#             chart_summary: Dict,
#     ) -> DbQuizSummary:
#         db_quiz_summary = DbQuizSummary(
#             token=Token.generate_quiz_answer_token(),
#             # SqlAlchemy won't immediately update the relationship fields, so we need to set it manually
#             quiz_id=db_quiz.id,
#             quiz=db_quiz,
#             chart_summary=chart_summary,
#         )
#         session.add(db_quiz_summary)
#         return db_quiz_summary
