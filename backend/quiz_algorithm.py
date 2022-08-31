from typing import Optional, Tuple

import numpy as np

from quiz_algorithm.constants import AlgorithmSubStep, AlgorithmStep, Step1SubSteps, Sign
from quiz_algorithm.models import QuizQuestion, QuizToken, QuestionToken, Question, Quiz, QuizAnswer, QuizQuestionToken, \
    Answer, AnswerToken


def TODO():
    raise NotImplementedError("TODO")


def require_not_none(nullable_variable, message):
    if nullable_variable is None:
        raise ValueError(message)


def require(predicate, message):
    if predicate():
        raise ValueError(message)


HEIGHT_QUESTION_TOKEN = QuestionToken("q_height")
BODY_SCHEMA_QUESTION_TOKEN = QuestionToken("q_body_schema")
EYE_COLOR_QUESTION_TOKEN = QuestionToken("q_eye_color")
HAIR_COLOR_QUESTION_TOKEN = QuestionToken("q_hair_color")


def get_dominant(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[0][0], sorted_scores[1][0], sorted_scores[2][0]


def get_next_non_asked_question_for_sign(sign: Sign) -> str:
    return None


def get_next_sign_for_question(
        last_step: AlgorithmStep,
        last_substep: AlgorithmSubStep,
        current_dm: Optional[Sign],
        scores: np.ndarray,
) -> Tuple[Sign, AlgorithmStep, AlgorithmSubStep]:
    scores = {
        'Огонь': fire,
        'Земля': earth,
        'Металл': metal,
        'Вода': water,
        'Дерево': wood,
    }

    if last_step == AlgorithmStep.STEP_1:
        require(lambda: int(last_substep) > int(Step1SubSteps.STEP1_SUBSTEP_40), "first 4 steps are handled elsewhere")

    # If it's the start of the questionnaire
    if last_step is None:
        return 1, 10, None

    dm, zn2, zn3 = get_dominant(scores)

    if last_substep == 40:  # After Цвет волос
        diff = scores[dm] - scores[zn2]
        if diff > 5:
            # Dm known, moving to step 2
            return 2, 10, dm
        elif scores[dm] == scores[zn2]:
            # Move to Подшаг 50 and 60
            return 1, 50, dm
        elif diff <= 5:
            # Recalculation using first two questions
            # ... here you'd integrate logic for recalculation based on the first two questions, which wasn't detailed in the provided algorithm
            # For now, we can return to 1, 50 for simplicity
            return 1, 50, dm
    elif last_substep in [50, 60, 70, 80]:
        # Assuming that we already asked the two additional questions to Dm and Zn2
        # and added those results to the total, we now have to check if we've got a dominant sign or if they're still tied
        if scores[dm] == scores[zn2]:
            return 1, 90, dm  # Here we're asking another question for the dominant sign
        else:
            return 2, 10, dm  # Move to next step with the dominant sign

    # Default (this should ideally never happen)
    return None, None, None


def get_next_question(
        last_step: Optional[AlgorithmStep],
        last_substep: Optional[AlgorithmSubStep],
        current_dm: Optional[Sign],
        scores: Optional[np.ndarray],
) -> Tuple[QuestionToken, AlgorithmStep, AlgorithmSubStep]:
    if last_step is None:
        require(lambda: last_substep is None, "last_substep must be None if last_step is None")
        return HEIGHT_QUESTION_TOKEN, AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_10

    require_not_none(last_substep, "last_substep must not be None if last_step is not None")

    if last_step == AlgorithmStep.STEP_1:
        if last_substep == Step1SubSteps.STEP1_SUBSTEP_10:
            return BODY_SCHEMA_QUESTION_TOKEN, AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_20

        if last_substep == Step1SubSteps.STEP1_SUBSTEP_20:
            return EYE_COLOR_QUESTION_TOKEN, AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_30

        if last_substep == Step1SubSteps.STEP1_SUBSTEP_30:
            return HAIR_COLOR_QUESTION_TOKEN, AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_40

    (next_sign, next_step, next_substep) = get_next_sign_for_question(last_step, last_substep, current_dm, scores)
    next_question_token = get_next_non_asked_question_for_sign(next_sign)
    return next_question_token, next_step, next_substep


def get_last_quiz_question(quiz_token: QuizToken) -> Optional[QuizQuestion]:
    TODO()


def get_last_quiz_answer(quiz_token: QuizToken) -> Optional[QuizAnswer]:
    TODO()


def get_question_by_token(next_question_toke: QuestionToken) -> Question:
    TODO()


def get_quiz_by_token(quiz_token: QuizToken) -> Quiz:
    pass


def api_get_next_question(quiz_token: QuizToken) -> QuizQuestion:
    quiz = get_quiz_by_token(quiz_token)
    last_quiz_question = get_last_quiz_question(quiz_token)
    last_quiz_answer = get_last_quiz_answer(quiz_token)

    if last_quiz_answer is None:
        if last_quiz_question is not None:
            # the user did not respond to the last question, ask again
            return last_quiz_question

        next_question_token, next_step, next_substep = get_next_question(
            last_step=None,
            last_substep=None,
            current_dm=None,
            scores=None,
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


def get_quiz_question_by_token(quiz_question_token: QuizQuestionToken) -> QuizQuestion:
    pass


def get_answer_by_token(answer_token: AnswerToken) -> Answer:
    pass


def api_post_question(quiz_question_token: QuizQuestionToken, answer_token: AnswerToken):
    quiz_question = get_quiz_question_by_token(quiz_question_token)
    answer = get_answer_by_token(answer_token)

    a = QuizAnswer(
        token="new",
        quiz_id=quiz_question.quiz_id,
        quiz_question_id=quiz_question.id,
        current_dominant_sign=current_dominant_sign,
        current_fire_sign_score=current_fire_sign_score,
        current_earth_sign_score=current_earth_sign_score,
        current_metal_sign_score=current_metal_sign_score,
        current_water_sign_score=current_water_sign_score,
        current_wood_sign_score=current_wood_sign_score,
    )