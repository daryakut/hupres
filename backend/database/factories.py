from database.database_utils import generate_user_token
from database.database_utils import generate_question_token
from database.database_utils import generate_answer_token
from database.database_utils import generate_quiz_token
from database.database_utils import generate_quiz_question_token
from database.database_utils import generate_quiz_answer_token
from database.db_models import DbUser
from database.db_models import DbQuestion
from database.db_models import DbAnswer
from database.db_models import DbQuiz
from database.db_models import DbQuizQuestion
from database.db_models import DbQuizAnswer
from quizzes.models import UserRole


def create_user(email_address: str, role: UserRole):
    return DbUser(
        token=generate_user_token(),
        email_address=email_address,
        role=role
    )


def create_question(question_name, is_tablet):
    return DbQuestion(
        token=generate_question_token(),
        question_name=question_name,
        is_tablet=is_tablet
    )


def create_answer(question_id, answer_name, sign_scores):
    return DbAnswer(
        token=generate_answer_token(),
        question_id=question_id,
        answer_name=answer_name,
        sign_scores=sign_scores
    )


def create_quiz(user_id, subject_name, pronounce, dm_after_step_1, dm_after_step_2, dm_after_step_3, dm_after_step_4):
    return DbQuiz(
        token=generate_quiz_token(),
        user_id=user_id,
        subject_name=subject_name,
        pronounce=pronounce,
        dm_after_step_1=dm_after_step_1,
        dm_after_step_2=dm_after_step_2,
        dm_after_step_3=dm_after_step_3,
        dm_after_step_4=dm_after_step_4
    )


def create_quiz_question(quiz_id, question_id, quiz_step, quiz_substep, followup_question_signs):
    return DbQuizQuestion(
        token=generate_quiz_question_token(),
        quiz_id=quiz_id,
        question_id=question_id,
        quiz_step=quiz_step,
        quiz_substep=quiz_substep,
        followup_question_signs=followup_question_signs
    )


def create_quiz_answer(quiz_id, quiz_question_id, answer_id, current_sign_scores, original_sign_scores):
    return DbQuizAnswer(
        token=generate_quiz_answer_token(),
        quiz_id=quiz_id,
        quiz_question_id=quiz_question_id,
        answer_id=answer_id,
        current_sign_scores=current_sign_scores,
        original_sign_scores=original_sign_scores
    )
