from enum import Enum
from typing import List, Optional

import numpy as np
from pydantic import BaseModel

from quizzes.constants import Sign
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


# Model for 'questions' table
class Question(BaseModel):
    token: str
    question_name: str
    is_tablet: bool


# Model for 'answers' table
class Answer22(BaseModel):
    token: str
    question_token: str
    answer_name: str
    sign_scores: List[int]


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


class Answer(BaseModel):
    answer_name: str
    display_answer: str


class QuizQuestion(BaseModel):
    token: str
    question_name: QuestionName
    display_question: str


# Model for 'quiz_answers' table
class QuizAnswer2(BaseModel):
    token: str
    quiz_id: int
    quiz_question_id: int
    answer_id: int
    current_sign_scores: List[int]
    # In some steps (e.g. step 1) we need to re-calculate the current scores and redefined them
    original_sign_scores: List[int]

    def get_scores(self) -> np.ndarray:
        return np.array(self.current_sign_scores)
