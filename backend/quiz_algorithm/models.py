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


class UserToken(BaseModel):
    value: str


class EmailAddress(BaseModel):
    value: str


# Model for 'users' table
class User(BaseModel):
    id: int
    token: UserToken
    email_address: EmailAddress
    role: UserRole = UserRole.ADMIN


class QuestionToken(BaseModel):
    value: str


# Model for 'questions' table
class Question(BaseModel):
    id: int
    token: QuestionToken
    question_name: str
    is_tablet: bool


class AnswerToken(BaseModel):
    value: str


# Model for 'answers' table
class Answer(BaseModel):
    id: int
    token: AnswerToken
    question_id: int
    answer_name: str
    fire_sign_score: int
    earth_sign_score: int
    metal_sign_score: int
    water_sign_score: int
    wood_sign_score: int


class QuizToken(BaseModel):
    value: str


# Model for 'quizzes' table
class Quiz(BaseModel):
    id: int
    token: QuizToken
    user_id: int
    subject_name: str
    pronounce: Pronounce
    dm_after_step_1: Sign
    dm_after_step_2: Sign
    dm_after_step_3: Sign
    dm_after_step_4: Sign


class QuizQuestionToken(BaseModel):
    value: str


class QuizAnswerToken(BaseModel):
    value: str


# Model for 'quiz_questions' table
class QuizQuestion(BaseModel):
    id: int
    token: QuizQuestionToken
    quiz_id: int
    question_id: int
    quiz_step: int
    quiz_substep: int
    followup_question_signs: List[Sign]


# Model for 'quiz_answers' table
class QuizAnswer(BaseModel):
    id: int
    token: QuizAnswerToken
    quiz_id: int
    quiz_question_id: int
    answer_id: int
    # current_dm: Optional[Sign] = None
    # current_zn2: Optional[Sign] = None
    # current_zn3: Optional[Sign] = None
    current_fire_sign_score: int
    current_earth_sign_score: int
    current_metal_sign_score: int
    current_water_sign_score: int
    current_wood_sign_score: int
    current_sign_scores: List[int]
    # In some steps (e.g. step 1) we need to re-calculate the current scores and redefined them
    original_sign_scores: List[int]
    # next_quiz_step: AlgorithmStep
    # next_quiz_substep: AlgorithmSubStep
    signs_for_next_questions: List[Sign]

    def get_scores(self) -> np.ndarray:
        return np.array([
            self.current_fire_sign_score,
            self.current_earth_sign_score,
            self.current_metal_sign_score,
            self.current_water_sign_score,
            self.current_wood_sign_score,
        ])
