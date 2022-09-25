from __future__ import annotations

from typing import Tuple, List

import numpy as np
from pydantic import BaseModel

from quizzes.common import check, check_not_none
from quizzes.constants import AlgorithmSubStep, AlgorithmStep, Step1SubSteps, Sign, Step2SubSteps, Step3SubSteps, \
    Step4SubSteps, Step5SubSteps, Step6SubSteps
from quizzes.models import QuizQuestion, QuizToken, QuestionToken, Quiz, QuizAnswer
from quizzes.queries import get_next_non_asked_question_for_sign, get_last_quiz_answer, get_last_quiz_question, \
    get_quiz_by_token, get_first_two_non_zero_tablet_answers

HEIGHT_QUESTION_TOKEN = QuestionToken(value="q_height")
BODY_SCHEMA_QUESTION_TOKEN = QuestionToken(value="q_body_schema")
EYE_COLOR_QUESTION_TOKEN = QuestionToken(value="q_eye_color")
HAIR_COLOR_QUESTION_TOKEN = QuestionToken(value="q_hair_color")


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


def get_dominant_four(scores: np.ndarray) -> Tuple[SignWithScore, SignWithScore, SignWithScore, SignWithScore]:
    pass


def get_next_signs_for_questions(
        quiz: Quiz,
        last_question: QuizQuestion,
        last_answer: QuizAnswer,
) -> Tuple[List[Sign], AlgorithmStep, AlgorithmSubStep]:
    last_step = last_question.quiz_step

    # First four questions of Step 1 are handled separately, so here we only handle the remaining questions in it
    if last_step == AlgorithmStep.STEP_1:
        return get_next_signs_for_questions_step1(
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    # We don't have conditions to get to step 2 in this exact method because `get_next_signs_for_questions_step1`
    # will redirect to step 2 if needed

    if last_step == AlgorithmStep.STEP_2:
        return get_next_signs_for_questions_step3(
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    if last_step == AlgorithmStep.STEP_3:
        return get_next_signs_for_questions_step4(
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    if last_step == AlgorithmStep.STEP_4:
        return get_next_signs_for_questions_step5(
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    if last_step == AlgorithmStep.STEP_5:
        return get_next_signs_for_questions_step6(
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    raise Exception("Unknown step")


def get_next_signs_for_questions_step1(
        quiz: Quiz,
        last_question: QuizQuestion,
        last_answer: QuizAnswer,
) -> Tuple[List[Sign], AlgorithmStep, AlgorithmSubStep]:
    last_step = last_question.quiz_step
    check(last_step == AlgorithmStep.STEP_1, "Step 1 is not active")

    last_substep = last_question.quiz_substep
    check(lambda: int(last_substep) > int(Step1SubSteps.STEP1_SUBSTEP_40), "First 4 questions are asked elsewhere")

    dm, zn2, zn3 = get_dominant(last_answer.get_scores())
    if last_substep == Step1SubSteps.STEP1_SUBSTEP_40:
        # Step 1.1
        # We have just received answers for first 4 tablet questions
        if dm.score > zn2.score + 5:
            # Step 1.1a
            # Dm is already determined known, moving to step 2
            quiz.dm_after_step_1 = dm.sign
            return get_next_signs_for_questions_step2(
                quiz=quiz,
                last_question=last_question,
                last_answer=last_answer,
            )

        if dm.score == zn2.score:
            # Step 1.1b
            # We need more information to determined Dm on step 1
            return [dm.sign, zn2.sign], AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_50_60

        # Step 1.1c
        first_two_non_zero_tablet_answers = get_first_two_non_zero_tablet_answers(quiz.token)
        if len(first_two_non_zero_tablet_answers) < 2:
            raise Exception("Not enough information to proceed with the quiz")
        # We store the original sign scores for the last answer just in case
        last_answer.original_sign_scores = last_answer.current_sign_scores
        # We redefined the original sign scores for the last answer based on the first two questions
        # Scores in the second of the two questions is going to contain the sum of scores for both
        last_answer.current_sign_scores = first_two_non_zero_tablet_answers[1].current_sign_scores

    if last_substep == Step1SubSteps.STEP1_SUBSTEP_40 or last_substep == Step1SubSteps.STEP1_SUBSTEP_50_60:
        # Step 2.2
        dm, zn2, zn3 = get_dominant(last_answer.get_scores())
        if dm.score > zn2.score:
            # Step 2.2a
            # TODO: here we need to record that DM is dm
            # Dm is determined to be the largest one, moving to step 2
            quiz.dm_after_step_1 = dm.sign
            return get_next_signs_for_questions_step2(
                quiz=quiz,
                last_question=last_question,
                last_answer=last_answer,
            )

        # Step 2.2b
        # We need more information to determine Dm on step 1
        return [dm.sign, zn2.sign], AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_70_80

    if last_substep == Step1SubSteps.STEP1_SUBSTEP_70_80:
        dm, zn2, zn3 = get_dominant(last_answer.get_scores())
        if dm.score > zn2.score:
            # Step 2.2b.i
            # TODO: here we need to record that DM is dm
            # Dm is determined to be the largest one, moving to step 2
            quiz.dm_after_step_1 = dm.sign
            return get_next_signs_for_questions_step2(
                quiz=quiz,
                last_question=last_question,
                last_answer=last_answer,
            )

        # Step 2.2b.ii
        # We need more information to determine Dm on step 1
        return [dm.sign, zn2.sign], AlgorithmStep.STEP_1, Step1SubSteps.STEP1_SUBSTEP_90_100

    if last_substep == Step1SubSteps.STEP1_SUBSTEP_90_100:
        dm, zn2, zn3 = get_dominant(last_answer.get_scores())
        quiz.dm_after_step_1 = dm.sign
        # TODO: here we need to record that DM is dm
        return get_next_signs_for_questions_step2(
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    raise Exception("Unknown substep")


def get_next_signs_for_questions_step2(
        quiz: Quiz,
        last_question: QuizQuestion,
        last_answer: QuizAnswer,
) -> Tuple[List[Sign], AlgorithmStep, AlgorithmSubStep]:
    last_step = last_question.quiz_step
    check(last_step == AlgorithmStep.STEP_1, "Step 1 is not active")

    # On the first step we have determined Dm, now we ask additional questions
    dm, zn2, zn3 = get_dominant(last_answer.get_scores())
    return [dm.sign, dm.sign], AlgorithmStep.STEP_2, Step2SubSteps.STEP2_SUBSTEP_10_20


def get_next_signs_for_questions_step3(
        quiz: Quiz,
        last_question: QuizQuestion,
        last_answer: QuizAnswer,
) -> Tuple[List[Sign], AlgorithmStep, AlgorithmSubStep]:
    last_step = last_question.quiz_step
    check(last_step == AlgorithmStep.STEP_2, "Step 2 is not active")

    # It means that we have answers for both questions for Step 2
    dm, zn2, zn3 = get_dominant(last_answer.get_scores())
    quiz.dm_after_step_2 = dm.sign

    # Now we are on Step 3
    if dm.score == zn2.score and zn2.score == zn3.score:
        # Step 3.4
        return [dm.sign, zn2.sign, zn3.sign], AlgorithmStep.STEP_3, Step3SubSteps.STEP3_SUBSTEP_110_120_130

    if dm.score == zn2.score:
        # Step 3.3
        # We want to ask two questions to the sign that was not dominant on Step 1
        if quiz.dm_after_step_1 == dm.sign:
            new_dm = zn2.sign
        else:
            new_dm = dm.sign
        return [new_dm, new_dm], AlgorithmStep.STEP_3, Step3SubSteps.STEP3_SUBSTEP_90_100

    if quiz.dm_after_step_1 != dm.sign:
        # Step 3.2
        return [dm.sign, dm.sign], AlgorithmStep.STEP_3, Step3SubSteps.STEP3_SUBSTEP_70_80

    # Step 3.1
    if dm.score > zn2.score + 5 and zn2.score > zn3.score + 3:
        # Step 3.1a
        return [zn2.sign, zn2.sign], AlgorithmStep.STEP_3, Step3SubSteps.STEP3_SUBSTEP_10_20

    if dm.score > zn2.score + 5:
        # Step 3.1b
        return [zn2.sign, zn3.sign], AlgorithmStep.STEP_3, Step3SubSteps.STEP3_SUBSTEP_30_40

    # Step 3.1c
    # this has exactly the same logic as the substep before, but just to be consistent with the Notion doc
    # we are writing it as a separate condition
    return [zn2.sign, zn3.sign], AlgorithmStep.STEP_3, Step3SubSteps.STEP3_SUBSTEP_50_60


def get_next_signs_for_questions_step4(
        quiz: Quiz,
        last_question: QuizQuestion,
        last_answer: QuizAnswer,
) -> Tuple[List[Sign], AlgorithmStep, AlgorithmSubStep]:
    last_step = last_question.quiz_step
    check(last_step == AlgorithmStep.STEP_3, "Step 3 is not active")

    # On the first step we have determined Dm, now we ask additional questions
    # In the doc this is still at the end of Step 3
    dm, zn2, zn3 = get_dominant(last_answer.get_scores())
    quiz.dm_after_step_3 = dm.sign

    if dm.score == zn2.score:
        # Step 4.3
        return [dm.sign, zn2.sign], AlgorithmStep.STEP_4, Step4SubSteps.STEP4_SUBSTEP_70_80

    if quiz.dm_after_step_3 != dm.sign:
        # Step 4.2
        return [dm.sign, dm.sign], AlgorithmStep.STEP_4, Step4SubSteps.STEP4_SUBSTEP_50_60

    # Step 4.1
    if zn2.score > zn3.score + 3:
        # Step 4.1a
        return [zn3.sign, zn3.sign], AlgorithmStep.STEP_4, Step4SubSteps.STEP4_SUBSTEP_10_20

    # Step 4.1b
    return [zn2.sign, zn3.sign], AlgorithmStep.STEP_4, Step4SubSteps.STEP4_SUBSTEP_30_40


def get_next_signs_for_questions_step5(
        quiz: Quiz,
        last_question: QuizQuestion,
        last_answer: QuizAnswer,
) -> Tuple[List[Sign], AlgorithmStep, AlgorithmSubStep]:
    last_step = last_question.quiz_step
    check(last_step == AlgorithmStep.STEP_4, "Step 4 is not active")

    # On the first step we have determined Dm, now we ask additional questions
    # In the doc this is still at the end of Step 3
    dm, zn2, zn3 = get_dominant(last_answer.get_scores())
    quiz.dm_after_step_4 = dm.sign

    if dm.score == zn2.score:
        # Step 5.3
        return [dm.sign, zn2.sign], AlgorithmStep.STEP_5, Step5SubSteps.STEP5_SUBSTEP_90_100

    if quiz.dm_after_step_4 != dm.sign:
        # Step 5.2
        return [dm.sign, dm.sign], AlgorithmStep.STEP_5, Step5SubSteps.STEP5_SUBSTEP_70_80

    # Step 5.1
    return [dm.sign, zn2.sign, zn3.sign], AlgorithmStep.STEP_5, Step5SubSteps.STEP5_SUBSTEP_10_20_30


def get_next_signs_for_questions_step6(
        quiz: Quiz,
        last_question: QuizQuestion,
        last_answer: QuizAnswer,
) -> Tuple[List[Sign], AlgorithmStep, AlgorithmSubStep]:
    last_step = last_question.quiz_step
    check(last_step == AlgorithmStep.STEP_5, "Step 5 is not active")

    # On the first step we have determined Dm, now we ask additional questions
    # In the doc this is still at the end of Step 3
    dm, zn2, zn3 = get_dominant(last_answer.get_scores())
    return [dm.sign, zn2.sign, zn3.sign], AlgorithmStep.STEP_6, Step6SubSteps.STEP6_SUBSTEP_10_20_30


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
    check_not_none(last_answer, "There is no answer for the last question. This indicates a bug")

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
