from __future__ import annotations
from __future__ import annotations

from typing import Dict, List

from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy import JSON
from sqlalchemy.orm import relationship

from database.connection import DbBase, Session
from database.db_entities.db_quiz import DbQuiz
from models.quiz_models import QuizProfileSummary, QuizSummary

EXCLUDE_PROFILES = {1, 27, 37, 44, 45, 46, 48}


class DbQuizSummary(DbBase):
    __tablename__ = 'quiz_summaries'
    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    chart_summary = Column(JSON)

    quiz = relationship('DbQuiz', back_populates='quiz_summaries', lazy='select')

    def to_model(self) -> QuizSummary:
        # print('summaries', self.chart_summary)

        summaries = []
        for profile in self.chart_summary:
            if profile['id'] in EXCLUDE_PROFILES:
                continue

            profile_summaries = []
            for profile_item_summary in profile.get('properties', []):
                name = profile_item_summary.get('name')
                text = profile_item_summary.get('text')
                if not name or not text or text == 'Коридор нормы':
                    continue
                # profile_summaries.append(f"{name}: {text}")
                profile_summaries.append(f"{text} ")

            summaries.append(
                QuizProfileSummary(
                    title=profile.get('name', ''),
                    summary='\n'.join(profile_summaries),
                )
            )
        return QuizSummary(
            summaries=summaries,
        )

    @staticmethod
    def create_quiz_summary(
            session: Session,
            db_quiz: DbQuiz,
            chart_summary: List[Dict],
    ) -> DbQuizSummary:
        db_quiz_summary = DbQuizSummary(
            # SqlAlchemy won't immediately update the relationship fields, so we need to set it manually
            quiz_id=db_quiz.id,
            quiz=db_quiz,
            chart_summary=chart_summary,
        )
        session.add(db_quiz_summary)
        return db_quiz_summary
