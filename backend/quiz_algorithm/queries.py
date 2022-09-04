from __future__ import annotations

from typing import Optional, List

from quiz_algorithm.constants import Sign
from quiz_algorithm.models import QuizQuestion, QuizToken, QuestionToken, Question, Quiz, QuizAnswer, QuizQuestionToken, \
    Answer, AnswerToken


def get_next_non_asked_question_for_sign(sign: Sign) -> str:
    pass


def get_quiz_by_token(quiz_token: QuizToken) -> Quiz:
    pass


def get_first_two_non_zero_tablet_answers(quiz_token: QuizToken) -> List[QuizAnswer]:
    pass


def get_quiz_question_by_token(quiz_question_token: QuizQuestionToken) -> QuizQuestion:
    pass


def get_answer_by_token(answer_token: AnswerToken) -> Answer:
    pass


def get_last_quiz_question(quiz_token: QuizToken) -> Optional[QuizQuestion]:
    pass


def get_last_quiz_answer(quiz_token: QuizToken) -> Optional[QuizAnswer]:
    pass


def get_last_quiz_answer_by_quiz_id(quiz_id: int) -> Optional[QuizAnswer]:
    pass


def get_question_by_token(next_question_toke: QuestionToken) -> Question:
    pass
