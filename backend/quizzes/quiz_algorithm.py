from __future__ import annotations

from common.translations import _
from typing import Tuple, List, Optional

from pydantic import BaseModel

from common.exceptions import Unauthorized
from common.utils import check
from database.connection import Session
from database.db_entities.db_quiz import DbQuiz
from database.db_entities.db_quiz_answer import DbQuizAnswer
from database.db_entities.db_quiz_question import DbQuizQuestion
from database.queries.quiz_answer_queries import QuizAnswerQueries
from database.queries.quiz_queries import QuizQueries
from database.queries.quiz_question_queries import QuizQuestionQueries
from database.transaction import transaction
from models.quiz_models import QuizQuestion, AvailableAnswer, Quiz, QuizAnswer
from models.sign import Sign
from models.token import Token
from quizzes.quiz_steps import QuizStep, QuizSubStep
from quizzes.question_database import QUESTION_NAMES_FOR_SIGNS, ANSWER_SCORES, QuestionName, MULTIPLE_CHOICE_QUESTIONS, \
    ANSWER_EXPLANATIONS, ANSWER_IMAGE_LINKS
from users.sessions import session_data_provider


class SignWithScore(BaseModel):
    sign: Sign
    score: int

    @staticmethod
    def from_sign_and_score(sign_value_and_score: Tuple[int, int]) -> SignWithScore:
        return SignWithScore(sign=Sign.from_index(sign_value_and_score[0]), score=sign_value_and_score[1])


def get_dominant(scores: List[int]) -> Tuple[SignWithScore, SignWithScore, SignWithScore]:
    indexed_scores = list(enumerate(scores))
    sorted_index_score_pairs = sorted(
        indexed_scores,
        # Fancy way to sort by score first, then index, so that sorting is consistent
        key=lambda index_and_value: index_and_value[1] * 1000 + index_and_value[0],
        reverse=True,
    )
    return (
        SignWithScore.from_sign_and_score(sorted_index_score_pairs[0]),
        SignWithScore.from_sign_and_score(sorted_index_score_pairs[1]),
        SignWithScore.from_sign_and_score(sorted_index_score_pairs[2]),
    )


def get_next_signs_for_questions(
        session: Session,
        quiz: DbQuiz,
        last_question: DbQuizQuestion,
        last_answer: DbQuizAnswer,
) -> Tuple[List[Sign], QuizStep, QuizSubStep]:
    last_step = last_question.quiz_step

    # First four questions of Step 1 are handled separately, so here we only handle the remaining questions in it
    if last_step == QuizStep.STEP_1:
        return get_next_signs_for_questions_step1(
            session=session,
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    # We don't have conditions to get to step 2 in this exact method because `get_next_signs_for_questions_step1`
    # will redirect to step 2 if needed

    if last_step == QuizStep.STEP_2:
        return get_next_signs_for_questions_step3(
            session=session,
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    if last_step == QuizStep.STEP_3:
        return get_next_signs_for_questions_step4(
            session=session,
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    if last_step == QuizStep.STEP_4:
        return get_next_signs_for_questions_step5(
            session=session,
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    if last_step == QuizStep.STEP_5:
        return get_next_signs_for_questions_step6(
            session=session,
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    raise Exception("Unknown step")


def get_next_signs_for_questions_step1(
        session: Session,
        quiz: DbQuiz,
        last_question: DbQuizQuestion,
        last_answer: DbQuizAnswer,
) -> Tuple[List[Sign], QuizStep, QuizSubStep]:
    last_step = last_question.quiz_step
    check(lambda: last_step == QuizStep.STEP_1, "Step 1 is not active")

    last_substep = last_question.quiz_substep
    # check(lambda: int(last_substep) > int(QuizSubStep.STEP1_SUBSTEP_40), "First 4 questions are asked elsewhere")
    check(
        lambda: last_substep not in [QuizSubStep.STEP1_SUBSTEP_10, QuizSubStep.STEP1_SUBSTEP_20,
                                     QuizSubStep.STEP1_SUBSTEP_30],
        "First 4 questions are asked elsewhere"
    )

    dm, zn2, zn3 = get_dominant(last_answer.current_sign_scores)
    if last_substep == QuizSubStep.STEP1_SUBSTEP_40:
        # Step 1.1
        # We have just received answers for first 4 tablet questions
        if dm.score > zn2.score + 3:
            # Step 1.1a
            # Dm is already determined known, moving to step 2
            quiz.dm_after_step_1 = dm.sign
            return get_next_signs_for_questions_step2(
                session=session,
                quiz=quiz,
                last_question=last_question,
                last_answer=last_answer,
            )

        # Step 1.1b
        # We need more information to determined Dm on step 1
        return [dm.sign, zn2.sign], QuizStep.STEP_1, QuizSubStep.STEP1_SUBSTEP_50_60

        # TODO: deprecated logic, remove
        # # Step 1.1c
        # first_two_non_zero_tablet_answers = QuizAnswerQueries.get_first_two_non_zero_tablet_answers(session, quiz.token)
        # if len(first_two_non_zero_tablet_answers) < 2:
        #     raise Exception("Not enough information to proceed with the quiz")
        # # We store the original sign scores for the last answer just in case
        # last_answer.original_sign_scores = last_answer.current_sign_scores
        # # We redefined the original sign scores for the last answer based on the first two questions
        # # Scores in the second of the two questions is going to contain the sum of scores for both
        # last_answer.current_sign_scores = first_two_non_zero_tablet_answers[1].current_sign_scores

    if last_substep == QuizSubStep.STEP1_SUBSTEP_40 or last_substep == QuizSubStep.STEP1_SUBSTEP_50_60:
        # Step 2.2
        dm, zn2, zn3 = get_dominant(last_answer.current_sign_scores)
        if dm.score > zn2.score:
            # Step 2.2a
            # TODO: here we need to record that DM is dm
            # Dm is determined to be the largest one, moving to step 2
            quiz.dm_after_step_1 = dm.sign
            return get_next_signs_for_questions_step2(
                session=session,
                quiz=quiz,
                last_question=last_question,
                last_answer=last_answer,
            )

        # Step 2.2b
        # We need more information to determine Dm on step 1
        return [dm.sign, zn2.sign], QuizStep.STEP_1, QuizSubStep.STEP1_SUBSTEP_70_80

    if last_substep == QuizSubStep.STEP1_SUBSTEP_70_80:
        dm, zn2, zn3 = get_dominant(last_answer.current_sign_scores)
        if dm.score > zn2.score:
            # Step 2.2b.i
            # TODO: here we need to record that DM is dm
            # Dm is determined to be the largest one, moving to step 2
            quiz.dm_after_step_1 = dm.sign
            return get_next_signs_for_questions_step2(
                session=session,
                quiz=quiz,
                last_question=last_question,
                last_answer=last_answer,
            )

        # Step 2.2b.ii
        # We need more information to determine Dm on step 1
        return [dm.sign, zn2.sign], QuizStep.STEP_1, QuizSubStep.STEP1_SUBSTEP_90_100

    if last_substep == QuizSubStep.STEP1_SUBSTEP_90_100:
        dm, zn2, zn3 = get_dominant(last_answer.current_sign_scores)
        quiz.dm_after_step_1 = dm.sign
        # TODO: here we need to record that DM is dm
        return get_next_signs_for_questions_step2(
            session=session,
            quiz=quiz,
            last_question=last_question,
            last_answer=last_answer,
        )

    raise Exception("Unknown substep")


def get_next_signs_for_questions_step2(
        session: Session,
        quiz: DbQuiz,
        last_question: DbQuizQuestion,
        last_answer: DbQuizAnswer,
) -> Tuple[List[Sign], QuizStep, QuizSubStep]:
    last_step = last_question.quiz_step
    check(lambda: last_step == QuizStep.STEP_1, "Step 1 is not active")

    # On the first step we have determined Dm, now we ask additional questions
    dm, zn2, zn3 = get_dominant(last_answer.current_sign_scores)
    return [dm.sign, dm.sign], QuizStep.STEP_2, QuizSubStep.STEP2_SUBSTEP_10_20


def get_next_signs_for_questions_step3(
        session: Session,
        quiz: DbQuiz,
        last_question: DbQuizQuestion,
        last_answer: DbQuizAnswer,
) -> Tuple[List[Sign], QuizStep, QuizSubStep]:
    last_step = last_question.quiz_step
    check(lambda: last_step == QuizStep.STEP_2, "Step 2 is not active")

    # It means that we have answers for both questions for Step 2
    dm, zn2, zn3 = get_dominant(last_answer.current_sign_scores)
    quiz.dm_after_step_2 = dm.sign

    # Now we are on Step 3
    if dm.score == zn2.score and zn2.score == zn3.score:
        # Step 3.4
        return [dm.sign, zn2.sign, zn3.sign], QuizStep.STEP_3, QuizSubStep.STEP3_SUBSTEP_110_120_130

    if dm.score == zn2.score:
        # Step 3.3
        # We want to ask two questions to the sign that was not dominant on Step 1
        if quiz.dm_after_step_1 == dm.sign:
            new_dm = zn2.sign
        else:
            new_dm = dm.sign
        return [new_dm, new_dm], QuizStep.STEP_3, QuizSubStep.STEP3_SUBSTEP_90_100

    if quiz.dm_after_step_1 != dm.sign:
        # Step 3.2
        return [dm.sign, dm.sign], QuizStep.STEP_3, QuizSubStep.STEP3_SUBSTEP_70_80

    # Step 3.1
    if dm.score > zn2.score + 5 and zn2.score > zn3.score + 3:
        # Step 3.1a
        return [zn2.sign, zn2.sign], QuizStep.STEP_3, QuizSubStep.STEP3_SUBSTEP_10_20

    # Step 3.1b
    return [zn2.sign, zn3.sign], QuizStep.STEP_3, QuizSubStep.STEP3_SUBSTEP_30_40


def get_next_signs_for_questions_step4(
        session: Session,
        quiz: DbQuiz,
        last_question: DbQuizQuestion,
        last_answer: DbQuizAnswer,
) -> Tuple[List[Sign], QuizStep, QuizSubStep]:
    last_step = last_question.quiz_step
    check(lambda: last_step == QuizStep.STEP_3, "Step 3 is not active")

    # On the first step we have determined Dm, now we ask additional questions
    # In the doc this is still at the end of Step 3
    dm, zn2, zn3 = get_dominant(last_answer.current_sign_scores)
    quiz.dm_after_step_3 = dm.sign

    if dm.score == zn2.score:
        # Step 4.3
        return [dm.sign, zn2.sign], QuizStep.STEP_4, QuizSubStep.STEP4_SUBSTEP_70_80

    if quiz.dm_after_step_3 != dm.sign:
        # Step 4.2
        return [dm.sign, dm.sign], QuizStep.STEP_4, QuizSubStep.STEP4_SUBSTEP_50_60

    # Step 4.1
    if zn2.score > zn3.score + 3:
        # Step 4.1a
        return [zn3.sign, zn3.sign], QuizStep.STEP_4, QuizSubStep.STEP4_SUBSTEP_10_20

    # Step 4.1b
    return [zn2.sign, zn3.sign], QuizStep.STEP_4, QuizSubStep.STEP4_SUBSTEP_30_40


def get_next_signs_for_questions_step5(
        session: Session,
        quiz: DbQuiz,
        last_question: DbQuizQuestion,
        last_answer: DbQuizAnswer,
) -> Tuple[List[Sign], QuizStep, QuizSubStep]:
    last_step = last_question.quiz_step
    check(lambda: last_step == QuizStep.STEP_4, "Step 4 is not active")

    # On the first step we have determined Dm, now we ask additional questions
    # In the doc this is still at the end of Step 3
    dm, zn2, zn3 = get_dominant(last_answer.current_sign_scores)
    quiz.dm_after_step_4 = dm.sign

    if dm.score == zn2.score:
        # Step 5.3
        return [dm.sign, zn2.sign], QuizStep.STEP_5, QuizSubStep.STEP5_SUBSTEP_90_100

    if quiz.dm_after_step_4 != dm.sign:
        # Step 5.2
        return [dm.sign, dm.sign], QuizStep.STEP_5, QuizSubStep.STEP5_SUBSTEP_70_80

    # Step 5.1
    return [dm.sign, zn2.sign, zn3.sign], QuizStep.STEP_5, QuizSubStep.STEP5_SUBSTEP_10_20_30


def get_next_signs_for_questions_step6(
        session: Session,
        quiz: DbQuiz,
        last_question: DbQuizQuestion,
        last_answer: DbQuizAnswer,
) -> Tuple[List[Sign], QuizStep, QuizSubStep]:
    last_step = last_question.quiz_step
    check(lambda: last_step == QuizStep.STEP_5, "Step 5 is not active")

    # On the first step we have determined Dm, now we ask additional questions
    # In the doc this is still at the end of Step 3
    dm, zn2, zn3 = get_dominant(last_answer.current_sign_scores)
    return [dm.sign, zn2.sign, zn3.sign], QuizStep.STEP_6, QuizSubStep.STEP6_SUBSTEP_10_20_30


def has_asked_question(session: Session, db_quiz_questions: List[DbQuizQuestion], question_name: str) -> bool:
    return next(
        (True for db_quiz_question in db_quiz_questions if db_quiz_question.question_name == question_name),
        False,
    )


def find_next_non_asked_question_name_for_sign(
        session: Session,
        db_quiz_questions: List[DbQuizQuestion],
        sign: Sign,
) -> Optional[str]:
    sign_question_names = QUESTION_NAMES_FOR_SIGNS[sign.value]
    already_asked_question_names = set(db_quiz_question.question_name for db_quiz_question in db_quiz_questions)
    question_name_to_ask = next(
        (question_name for question_name in sign_question_names if question_name not in already_asked_question_names),
        None,
    )
    return question_name_to_ask


class QuestionToAsk(BaseModel):
    question_name: QuestionName
    quiz_step: QuizStep
    quiz_substep: QuizSubStep
    followup_question_signs: List[Sign] = []
    quiz_question_token: Optional[Token[QuizQuestion]] = None  # Not None if existing question needs to be asked again


def get_next_question_to_ask(session: Session, db_quiz: DbQuiz) -> Optional[QuestionToAsk]:
    db_quiz_questions = db_quiz.quiz_questions
    db_last_question: DbQuizQuestion = db_quiz_questions[-1] if db_quiz_questions else None
    # last_question
    # last_question = QuizQuestionQueries.find_last_by_quiz_token(session, quiz_token)

    if db_last_question is None:
        # First question of the quiz is always the same
        return QuestionToAsk(
            question_name=QuestionName.HEIGHT,
            quiz_step=QuizStep.STEP_1,
            quiz_substep=QuizSubStep.STEP1_SUBSTEP_10,
        )

    # db_quiz_answers = db_quiz.quiz_answers
    # db_last_answer: DbQuizAnswer = db_quiz_answers[-1] if db_quiz_answers else None
    # db_last_answer = get_last_quiz_answer(quiz_token)
    # # TODO: should we return last question?
    # check_not_none(db_last_answer, "There is no answer for the last question. This indicates a bug")
    db_last_question_answer = db_last_question.answer
    if db_last_question_answer is None:
        return QuestionToAsk(
            question_name=db_last_question.question_name,
            quiz_step=db_last_question.quiz_step,
            quiz_substep=db_last_question.quiz_substep,
            quiz_question_token=db_last_question.token,  # we should not ask the last question and not create new
        )

    last_step = db_last_question.quiz_step
    last_substep = db_last_question.quiz_substep

    already_determined_signs = db_last_question_answer.signs_for_next_questions[:]
    if not db_last_question_answer.is_all_zeros and already_determined_signs:
        # If the last answer was not all zeros, we need to ask the followup questions
        # Otherwise we ask for the same sign again
        already_determined_signs.pop(0)

    if already_determined_signs:
        next_sign_to_ask_question = already_determined_signs[0]
        # TODO: return already_determined_signs that still has the questions we need to ask in next rounds
        # TODO: where do we track already_determined_signs, on question or answer?
        next_question_name = find_next_non_asked_question_name_for_sign(
            session,
            db_quiz_questions,
            next_sign_to_ask_question,
        )
        if not next_question_name:
            print("WARN: could not find next question name for sign", next_sign_to_ask_question)
            return None
        # we carry over the last step and substep, since we're still asking questions from the same substep
        return QuestionToAsk(
            question_name=next_question_name,
            quiz_step=last_step,
            quiz_substep=last_substep,
            followup_question_signs=already_determined_signs,
        )

    if last_step == QuizStep.STEP_1:
        if last_substep == QuizSubStep.STEP1_SUBSTEP_10:
            return QuestionToAsk(
                question_name=QuestionName.BODY_SCHEME,
                quiz_step=QuizStep.STEP_1,
                quiz_substep=QuizSubStep.STEP1_SUBSTEP_20,
            )

        if last_substep == QuizSubStep.STEP1_SUBSTEP_20:
            return QuestionToAsk(
                question_name=QuestionName.EYE_COLOR,
                quiz_step=QuizStep.STEP_1,
                quiz_substep=QuizSubStep.STEP1_SUBSTEP_30,
            )

        if last_substep == QuizSubStep.STEP1_SUBSTEP_30:
            return QuestionToAsk(
                question_name=QuestionName.HAIR_COLOR,
                quiz_step=QuizStep.STEP_1,
                quiz_substep=QuizSubStep.STEP1_SUBSTEP_40,
            )

    if last_step == QuizStep.STEP_6:
        # None means we've reached the end of the quiz
        return None

    # (next_signs, next_step, next_substep) = get_next_signs_for_questions(
    next_signs, quiz_step, quiz_substep = get_next_signs_for_questions(
        session=session,
        quiz=db_quiz,
        last_question=db_last_question,
        last_answer=db_last_question_answer,
    )
    next_sign_to_ask_question = next_signs[0]
    next_question_name = find_next_non_asked_question_name_for_sign(
        session,
        db_quiz_questions,
        next_sign_to_ask_question,
    )
    if not next_question_name:
        print("WARN: could not find next question name for sign", next_sign_to_ask_question)
        return None

    # next_question_token = get_next_non_asked_question_for_sign(next_sign)
    # return QuestionToken(value=next_question_token), next_step, next_substep

    return QuestionToAsk(
        question_name=next_question_name,
        quiz_step=quiz_step,
        quiz_substep=quiz_substep,
        followup_question_signs=next_signs,
    )


class GetNextQuizQuestionResponse(BaseModel):
    quiz_question: Optional[QuizQuestion]
    available_answers: List[AvailableAnswer]
    is_multiple_choice: bool


def api_get_next_question(quiz_token: Token[Quiz]) -> GetNextQuizQuestionResponse:
    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, quiz_token)

        session_data = session_data_provider.get_current_session()
        if not session_data.is_owner_of(db_quiz):
            raise Unauthorized("You are not allowed to get questions of this quiz")

        question_to_ask = get_next_question_to_ask(session=session, db_quiz=db_quiz)
        if question_to_ask is None:
            return GetNextQuizQuestionResponse(
                quiz_question=None,
                available_answers=[],
                is_multiple_choice=False,
            )

        if question_to_ask.quiz_question_token is not None:
            db_quiz_question = QuizQuestionQueries.find_by_token(session, question_to_ask.quiz_question_token)
        else:
            # we need to create a new question
            db_quiz_question = DbQuizQuestion.create_quiz_question(
                session=session,
                db_quiz=db_quiz,
                question_name=question_to_ask.question_name,
                quiz_step=question_to_ask.quiz_step,
                quiz_substep=question_to_ask.quiz_substep,
                followup_question_signs=question_to_ask.followup_question_signs,
            )

        answer_option_scores = ANSWER_SCORES.get(question_to_ask.question_name)
        check(
            lambda: answer_option_scores is not None,
            f"Could not find answers for question {question_to_ask.question_name}",
        )

        answer_explanations = ANSWER_EXPLANATIONS.get(question_to_ask.question_name)
        answer_image_links = ANSWER_IMAGE_LINKS.get(question_to_ask.question_name)
        available_answers = [AvailableAnswer(
            answer_name=a,
            answer_display_name=_(a),
            answer_explanation=answer_explanations.get(a),
            answer_image_link=answer_image_links.get(a),
        ) for a in answer_option_scores.keys()]
        return GetNextQuizQuestionResponse(
            quiz_question=db_quiz_question.to_model(),
            available_answers=available_answers,
            is_multiple_choice=question_to_ask.question_name in MULTIPLE_CHOICE_QUESTIONS
        )


class SubmitAnswerResponse(BaseModel):
    quiz_answer: QuizAnswer
    current_sign_scores: List[int]


def api_submit_answers(quiz_question_token: Token[QuizQuestion], answer_names: List[str]) -> SubmitAnswerResponse:
    with transaction() as session:
        db_quiz_question = QuizQuestionQueries.find_by_token(session, quiz_question_token)
        db_quiz: DbQuiz = db_quiz_question.quiz

        session_data = session_data_provider.get_current_session()
        if not session_data.is_owner_of(db_quiz):
            raise Unauthorized("You are not allowed to submit answers to this quiz")

        check(
            lambda: db_quiz_question.answer is None,
            f"You have already responded to question {db_quiz_question.question_name}",
        )

        answer_option_scores = ANSWER_SCORES.get(db_quiz_question.question_name)
        check(
            lambda: answer_option_scores is not None,
            f"Could not find answers for question {db_quiz_question.question_name}",
        )

        answer_scores = [0, 0, 0, 0, 0]
        for answer_name in answer_names:
            current_answer_scores = answer_option_scores.get(answer_name)
            check(lambda: current_answer_scores is not None, f"Invalid answer name {answer_scores}")
            answer_scores = [sum(x) for x in zip(answer_scores, current_answer_scores)]

        db_last_answer = QuizAnswerQueries.find_last_for_quiz(session, db_quiz.token)
        last_sign_scores = db_last_answer.current_sign_scores if db_last_answer else [0, 0, 0, 0, 0]

        # Add new scores to already accumulated scores
        current_sign_scores = [sum(x) for x in zip(last_sign_scores, answer_scores)]

        is_all_zeros = all(score == 0 for score in answer_scores)
        db_quiz_answer = DbQuizAnswer.create_quiz_answer(
            session=session,
            db_quiz=db_quiz,
            db_quiz_question=db_quiz_question,
            answer_names=answer_names,
            is_all_zeros=is_all_zeros,
            current_sign_scores=current_sign_scores,
            signs_for_next_questions=db_quiz_question.followup_question_signs,
        )
        return SubmitAnswerResponse(
            quiz_answer=db_quiz_answer.to_model(),
            current_sign_scores=current_sign_scores,
        )
