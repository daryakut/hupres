import secrets
import re

from quiz_algorithm.models import Token

MAX_TOKEN_LENGTH = 20
NON_SMALL_LETTERS_OR_NUMBERS_REGEX = r'[^a-z0-9]'


def _generate_token(prefix: str) -> str:
    random_string = secrets.token_urlsafe(MAX_TOKEN_LENGTH)
    return f"{prefix}_" + re.sub(NON_SMALL_LETTERS_OR_NUMBERS_REGEX, '', random_string)


def generate_user_token() -> Token:
    return Token(value=_generate_token("u"))


def generate_question_token() -> Token:
    return Token(value=_generate_token("qu"))


def generate_answer_token() -> Token:
    return Token(value=_generate_token("an"))


def generate_quiz_token() -> Token:
    return Token(value=_generate_token("q"))


def generate_quiz_question_token() -> Token:
    return Token(value=_generate_token("qq"))


def generate_quiz_answer_token() -> Token:
    return Token(value=_generate_token("qa"))
