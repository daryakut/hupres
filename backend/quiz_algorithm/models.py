from enum import Enum
from typing import List

import numpy as np
from pydantic import BaseModel

from quiz_algorithm.constants import Sign

class UserRole(Enum):
    ADMIN = 'ADMIN'
    RESPONDENT = 'RESPONDENT'


# Instead of the gender, this is what western world uses. Hopefully that's enough
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
class Answer(BaseModel):
    token: str
    question_token: str
    answer_name: str
    sign_scores: List[int]


# Model for 'quizzes' table
class Quiz(BaseModel):
    token: str
    user_token: str
    subject_name: str
    pronounce: Pronounce
    dm_after_step_1: Sign
    dm_after_step_2: Sign
    dm_after_step_3: Sign
    dm_after_step_4: Sign


# Model for 'quiz_questions' table
class QuizQuestion(BaseModel):
    token: str
    quiz_id: int
    question_id: int
    quiz_step: int
    quiz_substep: int
    followup_question_signs: List[Sign]


# Model for 'quiz_answers' table
class QuizAnswer(BaseModel):
    token: str
    quiz_id: int
    quiz_question_id: int
    answer_id: int
    current_sign_scores: List[int]
    # In some steps (e.g. step 1) we need to re-calculate the current scores and redefined them
    original_sign_scores: List[int]

    def get_scores(self) -> np.ndarray:
        return np.array(self.current_sign_scores)
