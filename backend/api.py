from __future__ import annotations

import numpy as np

from quizzes.algorithm import get_next_question
from quizzes.constants import AlgorithmStep
from quizzes.models import QuizQuestion, QuizToken, QuizAnswer, QuizQuestionToken, \
    AnswerToken
from quizzes.queries import get_last_quiz_question, get_last_quiz_answer, get_quiz_by_token, \
    get_question_by_token, get_quiz_question_by_token, get_answer_by_token, get_last_quiz_answer_by_quiz_id


def api_get_next_question(quiz_token: QuizToken) -> QuizQuestion:
    last_quiz_question = get_last_quiz_question(quiz_token)
    last_quiz_answer = get_last_quiz_answer(quiz_token)
    quiz = get_quiz_by_token(quiz_token)

    if last_quiz_answer is None:
        if last_quiz_question is not None:
            # the user did not respond to the last question, ask again
            return last_quiz_question

        next_question_token, next_step, next_substep = get_next_question(
            last_question=None,
            last_answer=None,
        )
        new_question = get_question_by_token(next_question_token)
        return QuizQuestion(
            token="new",
            quiz_id=quiz.id,
            question_id=new_question.id,
            quiz_step=next_step,
            quiz_substep=next_substep,
        )

    last_step = AlgorithmStep(last_quiz_question.quiz_step)
    last_substep_class = last_step.get_substep_class()
    # last_substep_class is a class, so last_substep_class(...) is instantiation of the corresponding enum value
    last_substep = last_substep_class(last_quiz_question.quiz_substep)

    next_question_token, next_step, next_substep = get_next_question(
        last_step=last_step,
        last_substep=last_substep,
        current_dm=last_quiz_answer.current_dominant_sign,
        scores=np.ndarray([
            last_quiz_answer.current_fire_sign_score,
            last_quiz_answer.current_earth_sign_score,
            last_quiz_answer.current_metal_sign_score,
            last_quiz_answer.current_water_sign_score,
            last_quiz_answer.current_wood_sign_score,
        ]),
    )
    new_question = get_question_by_token(next_question_token)
    return QuizQuestion(
        token="new",
        quiz_id=quiz.id,
        question_id=new_question.id,
        quiz_step=next_step,
        quiz_substep=next_substep,
    )


def api_post_answer(quiz_question_token: QuizQuestionToken, answer_token: AnswerToken):
    quiz_question = get_quiz_question_by_token(quiz_question_token)
    answer = get_answer_by_token(answer_token)
    last_quiz_answer = get_last_quiz_answer_by_quiz_id(quiz_question.quiz_id)
    last_fire_sign_score = last_quiz_answer.current_fire_sign_score or
    last_earth_sign_score = last_quiz_answer.current_earth_sign_score or
    last_metal_sign_score = last_quiz_answer.current_metal_sign_score or
    last_water_sign_score = last_quiz_answer.current_water_sign_score or
    last_wood_sign_score = last_quiz_answer.current_wood_sign_score or

    quiz_answer = QuizAnswer(
        token="new",
        quiz_id=quiz_question.quiz_id,
        quiz_question_id=quiz_question.id,
        answer_id=answer.id,
        # current_dominant_sign=current_dominant_sign, ??
        current_fire_sign_score=last_quiz_answer.current_fire_sign_score + answer.fire_sign_score,
        current_earth_sign_score=last_quiz_answer.current_earth_sign_score + answer.earth_sign_score,
        current_metal_sign_score=last_quiz_answer.current_metal_sign_score + answer.metal_sign_score,
        current_water_sign_score=last_quiz_answer.current_water_sign_score + answer.water_sign_score,
        current_wood_sign_score=last_quiz_answer.current_wood_sign_score + answer.wood_sign_score,
    )
