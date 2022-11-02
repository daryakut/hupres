from enum import Enum
from typing import Optional

from pydantic import BaseModel

from models.sign import Sign
from quizzes.question_database import QuestionName


class UserRole(Enum):
    ADMIN = 'ADMIN'
    RESPONDENT = 'RESPONDENT'


# Instead of the gender, this is what western world uses. Hopefully these choices is enough
class Pronounce(Enum):
    HE_HIM = 'HE_HIM'
    SHE_HER = 'SHE_HER'
    THEY_THEM = 'THEY_THEM'
    PREFER_NOT_TO_SAY = 'PREFER_NOT_TO_SAY'


# Model for 'users' table
class User(BaseModel):
    token: str
    email_address: str
    role: UserRole = UserRole.ADMIN


# Model for 'quizzes' table
class Quiz(BaseModel):
    token: str
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
    display_answer: str


class QuizAnswer(BaseModel):
    """Representation of the DB object, whatever the Frontend might need to know about it"""
    token: str


class QuizQuestion(BaseModel):
    """Representation of the DB object, whatever the Frontend might need to know about it"""
    token: str
    question_name: QuestionName
    question_display_name: str
