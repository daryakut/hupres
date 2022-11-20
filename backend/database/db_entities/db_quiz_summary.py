from __future__ import annotations
from __future__ import annotations

import json
import re
from enum import Enum
from typing import Dict, List

from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy import JSON
from sqlalchemy.orm import relationship

from database.connection import DbBase, Session
from database.db_entities.db_quiz import DbQuiz
from database.db_entities.db_timestamped_entity import DbTimestampedEntity
from models.quiz_models import QuizSummary
from quizzes.charts.charts import NAME_PLACEHOLDER
from common.translations import _

K_SYMBOL_REGEX = r" К[1-5]"  # Some names have that, this is cyrillic
MN_POSTFIX = " (MH)"  # Some names have that too, this is cyrillic
# KN_POSTFIX = " (КН)"  # Some names have that too, this is cyrillic

BOOK_SUMMARY_PROFILES = {44, 45, 46, 48}
TEXTUAL_GPT_SUMMARY_QUALITIES = {
    # Тип эмоциональности
    11: {
        1, 11, 7, 59,
    },
    # Особенности мышления и восприятия
    12: {
        20, 21, 44, 35, 56,
    },
    # Особенности работоспособности
    13: {
        30, 32, 57, 34, 35, 37, 6,
    },
    # Коммуникации
    14: {
        24, 74, 82, 75, 46,
    },
    # Лидерство
    15: {
        139, 54, 53, 51,
    },
}
TEXTUAL_GPT_SUMMARY_QUALITIES_WITH_K = {
    # Оптимальный режим работы
    30: {
        157, 158, 159, 160, 161,
    },
    # Какую работу выполняет лучше
    33: {
        167, 168, 169, 170, 171,
    },
    # Как лучше доносить информацию
    35: {
        182, 183, 184, 185, 186,
    },
    # Нематериальная мотивация
    36: {
        177, 178, 179, 180, 181,
    },
    # Любит / Не любит
    29: {
        147, 148, 149, 150, 151, 152, 153, 154, 155, 156,
    },
}
RATED_GPT_SUMMARY_QUALITIES = {
    # Деловые качества
    21: {
        67, 66, 77, 144, 65, 87, 73, 70, 83, 84, 76, 79, 71, 9, 86,
    }
}
ALL_GPT_SUMMARY_QUALITIES = {
    **TEXTUAL_GPT_SUMMARY_QUALITIES,
    **TEXTUAL_GPT_SUMMARY_QUALITIES_WITH_K,
    **RATED_GPT_SUMMARY_QUALITIES,
}


class RatedValueText(Enum):
    LOW = 'низький показник'
    BELOW_AVERAGE = 'показник нижче середнього'
    ABOVE_AVERAGE = 'показник вище середнього'
    HIGH = 'високий показник'


def sanitize_name(name: str) -> str:
    return (re.sub(K_SYMBOL_REGEX, "", name)
            .replace(MN_POSTFIX, "")
            # .replace(KN_POSTFIX, "")
            .replace("*", ""))


def build_qualities_gpt_prompt(chart_summary: dict, subject_name: str) -> str:
    # print('GPT summaries', json.dumps(chart_summary))

    qualities = []
    for profile in chart_summary:
        profile_id = profile.get('id')
        eligible_property_ids = ALL_GPT_SUMMARY_QUALITIES.get(profile_id)
        if not eligible_property_ids:
            continue

        qualities.append(profile.get('name') + ":\n")
        for prop in profile.get('properties', []):
            if not prop.get('id') in eligible_property_ids:
                continue

            name = prop.get('name', '')
            sanitized_name = sanitize_name(name)

            if profile_id in TEXTUAL_GPT_SUMMARY_QUALITIES.keys():
                # Text should already contain textual representation of the quality
                text = prop.get('text')
                text = text.replace(NAME_PLACEHOLDER, subject_name)
                if not text:
                    print("ERROR: GPT property text is empty", prop.get('id'), sanitized_name)
                    continue
                quality_text = sanitized_name + ": " + text
            elif profile_id in TEXTUAL_GPT_SUMMARY_QUALITIES_WITH_K.keys():
                # With K1-K5 profiles, name is repeated and so it's unnecessary to include it
                quality_text = prop.get('text')
                quality_text = quality_text.replace(NAME_PLACEHOLDER, subject_name)
            else:
                # The quality is rated on a scale of 1 to 5, 1 being lowest and 5 being highest
                prop_value = prop.get('value')
                if prop_value <= 2:
                    text = RatedValueText.LOW.value
                elif prop_value <= 3:
                    text = RatedValueText.BELOW_AVERAGE.value
                elif prop_value <= 4:
                    text = RatedValueText.ABOVE_AVERAGE.value
                else:
                    text = RatedValueText.HIGH.value
                quality_text = sanitized_name + ": " + text

            qualities.append(quality_text)
        qualities.append("\n")
    return "\n".join(qualities)


class DbQuizSummary(DbTimestampedEntity, DbBase):
    __tablename__ = 'quiz_summaries'
    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    chart_summary = Column(JSON)

    quiz = relationship('DbQuiz', back_populates='quiz_summaries', lazy='select')

    def to_model_gpt_profile(self) -> str:
        return build_qualities_gpt_prompt(self.chart_summary, subject_name=self.quiz.subject_name)

    def to_model_book_profile(self) -> QuizSummary:
        # print('Book summaries', json.dumps(self.chart_summary))
        subject_name = self.quiz.subject_name
        summaries = []
        for profile in self.chart_summary:
            if profile['id'] not in BOOK_SUMMARY_PROFILES:
                continue

            profile_summaries = []
            for prop in profile.get('properties', []):
                name = sanitize_name(prop.get('name', ''))
                text = prop.get('text')
                if not name or not text:
                    continue

                # We first translate, and then we replace ZZZ with the respondent name
                text = _(text)
                text = text.replace(NAME_PLACEHOLDER, subject_name)
                # We only want to show the text without the name
                profile_summaries.append(f"{text}")

            summaries.append(" ".join(profile_summaries))

        print('Summaries', summaries)
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
