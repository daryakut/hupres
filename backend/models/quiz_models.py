from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from models.pronounce import Pronounce
from models.sign import Sign
from quizzes.question_database import QuestionName


class QuizSummary(BaseModel):
    """Textual representation of the DB object"""
    summaries: List[str]


class QuizFreeFormQuestion(BaseModel):
    """Textual representation of the DB object"""
    question: str
    answer: str


class Quiz(BaseModel):
    """Representation of the DB object, whatever the Frontend might need to know about it"""
    token: str
    created_at: Optional[str]  # When quiz is just created, this would be null due to how SqlAlchemy works
    # created_at: str
    user_token: Optional[str]
    subject_name: Optional[str]
    pronounce: Optional[Pronounce]
    dm_after_step_1: Optional[Sign]
    dm_after_step_2: Optional[Sign]
    dm_after_step_3: Optional[Sign]
    dm_after_step_4: Optional[Sign]


class AvailableAnswer(BaseModel):
    """Representation of the available answer from questions database"""
    answer_name: str
    answer_display_name: str


class QuizAnswer(BaseModel):
    """Representation of the DB object, whatever the Frontend might need to know about it"""
    token: str


class QuizQuestion(BaseModel):
    """Representation of the DB object, whatever the Frontend might need to know about it"""
    token: str
    question_name: QuestionName
    question_display_name: str
