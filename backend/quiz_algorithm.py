from typing import Optional, Tuple, List
from __future__ import annotations

import numpy as np
from pydantic import BaseModel

from quiz_algorithm.constants import AlgorithmSubStep, AlgorithmStep, Step1SubSteps, Sign, Step2SubSteps
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


def get_last_quiz_question(quiz_token: QuizToken) -> Optional[QuizQuestion]:
    TODO()


def get_last_quiz_answer(quiz_token: QuizToken) -> Optional[QuizAnswer]:
    TODO()


def get_last_quiz_answer_by_quiz_id(quiz_id: int) -> Optional[QuizAnswer]:
    TODO()


def get_question_by_token(next_question_toke: QuestionToken) -> Question:
    TODO()


class SignWithScore(BaseModel):
    sign: Sign
    score: int

    @staticmethod
    def from_sign_and_score(sign_value_and_score: Tuple[int, int]) -> SignWithScore:
        return SignWithScore(sign=Sign(sign_value_and_score[0]), score=sign_value_and_score[1])


def get_dominant(scores: np.ndarray) -> Tuple[SignWithScore, SignWithScore, SignWithScore]:
    # sorted_scores = np.sort(scores)
    indexed_scores = list(enumerate(scores))
    sorted_index_score_pairs = sorted(
        indexed_scores,
        # Fancy way to sort by score first, then index, so that sorting is consistent
        key=lambda index_and_value: index_and_value[1] * 1000 + index_and_value[0],
        reverse=True,
    )
    return (
        SignWithScore.from_sign_and_score(sorted_index_score_pairs[-1]),
        SignWithScore.from_sign_and_score(sorted_index_score_pairs[-2]),
        SignWithScore.from_sign_and_score(sorted_index_score_pairs[-3]),
    )


def get_next_non_asked_question_for_sign(sign: Sign) -> str:
    return None


def get_next_signs_for_questions(
        quiz: Quiz,
        last_question: QuizQuestion,
        last_answer: QuizAnswer,
) -> Tuple[List[Sign], AlgorithmStep, AlgorithmSubStep]:
# ) -> List[Sign]:
    last_step = last_question.quiz_step
    last_substep = last_question.quiz_substep

    if last_step == AlgorithmStep.STEP_1:
        require(lambda: int(last_substep) > int(Step1SubSteps.STEP1_SUBSTEP_40), "First 4 questions are asked elsewhere")

        dm, zn2, zn3 = get_dominant(last_answer.get_scores())
        if last_substep == Step1SubSteps.STEP1_SUBSTEP_40:
            diff = dm.score - zn2.score

            if diff > 5:
                # Dm known, moving to step 2
                # TODO: THIS FALLS THROUGH TO STEP 2
                quiz.dm_after_step_1 = dm.sign
                # return [dm.sign, dm.sign], AlgorithmStep.STEP_2, Step2SubSteps.STEP2_SUBSTEP_10_20
            if dm.score == zn2.score:
                return [dm.sign, zn2.sign], AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_50_60

            # Recalculate last_answer.get_scores() based on first two questions and fall through

        if last_substep == Step1SubSteps.STEP1_SUBSTEP_40 or last_substep == Step1SubSteps.STEP1_SUBSTEP_50_60:
            # we are here https://www.notion.so/1-cf4a40b40d874ecb9604b7a3a15c2405?pvs=4#7977f9bfe89f4ef8bdfca33d23f1c36b
            dm, zn2, zn3 = get_dominant(last_answer.get_scores())
            diff = dm.score - zn2.score
            if diff > 0:
                # TODO: here we need to record that DM is dm
                quiz.dm_after_step_1 = dm.sign
                # TODO: THIS FALLS THROUGH TO STEP 2

            # dm and zn2 are equal
            return [dm.sign, zn2.sign], AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_70_80

        if last_substep == Step1SubSteps.STEP1_SUBSTEP_70_80:
            dm, zn2, zn3 = get_dominant(last_answer.get_scores())
            diff = dm.score - zn2.score
            if diff > 0:
                # TODO: here we need to record that DM is dm
                return [dm.sign, dm.sign], AlgorithmStep.STEP_2, Step2SubSteps.STEP2_SUBSTEP_10_20

            return [dm.sign, zn2.sign], AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_90_100

        if last_substep == Step1SubSteps.STEP1_SUBSTEP_90_100:
            dm, zn2, zn3 = get_dominant(last_answer.get_scores())
            # TODO: here we need to record that DM is dm
            return [dm.sign, dm.sign], AlgorithmStep.STEP_2, Step2SubSteps.STEP2_SUBSTEP_10_20

        raise Exception("Unknown substep")

    if last_step == AlgorithmStep.STEP_2 or AlgorithmStep.STEP_1:
        # It means that we have answers for both questions for Step 2
        dm, zn2, zn3 = get_dominant(last_answer.get_scores())
        quiz.dm_after_step_1 = dm.sign

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
        quiz_token: QuizToken,
        # last_question: Optional[QuizQuestion],
        # last_answer: Optional[QuizAnswer],
        # last_step: Optional[AlgorithmStep],
        # last_substep: Optional[AlgorithmSubStep],
        # current_dm: Optional[Sign],
        # scores: Optional[np.ndarray],
) -> Tuple[QuestionToken, AlgorithmStep, AlgorithmSubStep]:
    quiz = get_quiz_by_token(quiz_token)
    last_question = get_last_quiz_question(quiz_token)

    if last_question is None:
        # First question of the quiz is always the same
        return HEIGHT_QUESTION_TOKEN, AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_10

    last_answer = get_last_quiz_answer(quiz_token)
    require_not_none(last_answer, "There is no answer for the last question. This indicates a bug")

    last_step = last_question.quiz_step
    last_substep = last_question.quiz_substep

    already_determined_signs = last_answer.signs_for_next_questions
    if already_determined_signs:
        next_sign_to_ask_question = already_determined_signs.pop(0)
        # TODO: return already_determined_signs that still has the questions we need to ask in next rounds
        next_question_token = get_next_non_asked_question_for_sign(next_sign_to_ask_question)
        # we carry over the last step and substep, since we're still asking questions from the same substep
        QuestionToken(value=next_question_token), last_step, last_substep

    if last_step == AlgorithmStep.STEP_1:
        if last_substep == Step1SubSteps.STEP1_SUBSTEP_10:
            return BODY_SCHEMA_QUESTION_TOKEN, AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_20

        if last_substep == Step1SubSteps.STEP1_SUBSTEP_20:
            return EYE_COLOR_QUESTION_TOKEN, AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_30

        if last_substep == Step1SubSteps.STEP1_SUBSTEP_30:
            return HAIR_COLOR_QUESTION_TOKEN, AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_40

        # if last_substep == Step1SubSteps.STEP1_SUBSTEP_40:
        #     return HAIR_COLOR_QUESTION_TOKEN, AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_40

    # (next_signs, next_step, next_substep) = get_next_signs_for_questions(
    next_signs = get_next_signs_for_questions(
        quiz=quiz,
        last_question=last_question,
        last_answer=last_answer,
    )
    next_question_token = get_next_non_asked_question_for_sign(next_sign)
    return QuestionToken(value=next_question_token), next_step, next_substep

def get_quiz_by_token(quiz_token: QuizToken) -> Quiz:
    pass


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


def get_quiz_question_by_token(quiz_question_token: QuizQuestionToken) -> QuizQuestion:
    pass


def get_answer_by_token(answer_token: AnswerToken) -> Answer:
    pass


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
