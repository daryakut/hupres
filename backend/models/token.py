from __future__ import annotations

import re
import secrets
from typing import TypeVar, Generic

from quizzes.models import User, Question, Answer, Quiz, QuizQuestion, QuizAnswer

# Define the types for which the Token can be used
T = TypeVar('T', bound='Base')  # T is bounded to the Base class

MAX_TOKEN_LENGTH = 10
MAX_SESSION_TOKEN_LENGTH = 50
NON_SMALL_LETTERS_OR_NUMBERS_REGEX = r'[^a-z0-9]'


class Token(Generic[T]):
    value: str

    def __init__(self, value: str):
        self.value = value

    @staticmethod
    def of(value) -> Token[T]:
        return Token(value)

    @staticmethod
    def _generate_token(prefix: str) -> Token[T]:
        random_string = secrets.token_urlsafe(MAX_TOKEN_LENGTH)
        return Token(f"{prefix}_" + re.sub(NON_SMALL_LETTERS_OR_NUMBERS_REGEX, '', random_string))

    @staticmethod
    def generate_user_token() -> Token[User]:
        return Token._generate_token("u")

    @staticmethod
    def generate_question_token() -> Token[Question]:
        return Token._generate_token("qu")

    @staticmethod
    def generate_answer_token() -> Token[Answer]:
        return Token._generate_token("an")

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
