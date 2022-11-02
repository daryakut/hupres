from __future__ import annotations

import re
import secrets
from typing import TypeVar, Generic

from pydantic import BaseModel

from models.quiz_models import Quiz, QuizQuestion, QuizAnswer
from models.user import User

# from pydantic.generics import GenericModel, TypeVarModel

# T = TypeVarModel("T")

# # Define the types for which the Token can be used
# T = TypeVar('T', bound='Base')  # T is bounded to the Base class
T = TypeVar("T", bound=BaseModel)

MAX_TOKEN_LENGTH = 10
MAX_SESSION_TOKEN_LENGTH = 50
NON_SMALL_LETTERS_OR_NUMBERS_REGEX = r'[^a-z0-9]'


# @dataclass(frozen=True)
class Token(BaseModel, Generic[T]):
    value: str

    # def __init__(self, value: str):
    #     self.value = value

    # def __eq__(self, other):
    #     return self.value == other.value

    @staticmethod
    def of(value) -> Token[T]:
        return Token(value=value)

    @staticmethod
    def _generate_token(prefix: str) -> Token[T]:
        random_string = secrets.token_urlsafe(MAX_TOKEN_LENGTH)
        value = f"{prefix}_" + re.sub(NON_SMALL_LETTERS_OR_NUMBERS_REGEX, '', random_string)
        return Token(value=value)

    @staticmethod
    def generate_user_token() -> Token[User]:
        return Token._generate_token("u")

    @staticmethod
    def generate_quiz_token() -> Token[Quiz]:
        return Token._generate_token("q")

    @staticmethod
    def generate_quiz_question_token() -> Token[QuizQuestion]:
        return Token._generate_token("qq")

    @staticmethod
    def generate_quiz_answer_token() -> Token[QuizAnswer]:
        return Token._generate_token("qa")


def generate_session_token() -> str:
    random_string = secrets.token_urlsafe(MAX_SESSION_TOKEN_LENGTH)
    return re.sub(NON_SMALL_LETTERS_OR_NUMBERS_REGEX, '', random_string)
