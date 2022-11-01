import pytest

from common.clock import clock
from common.exceptions import BadRequest, Unauthorized
from database.db_quiz import DbQuiz
from database.quiz_queries import QuizQueries
from database.quiz_question_queries import QuizQuestionQueries
from database.transaction import transaction
from quizzes.constants import QuizStep, QuizSubStep
from quizzes.question_database import BODY_SCHEMA_QUESTION_NAME, HEIGHT_QUESTION_NAME
from tests.test_utils.user_tester import UserTester


def setup_module(module):
    print(f"Setting up for {module.__name__}")


@pytest.mark.asyncio
async def test_can_get_first_question():
    user_tester = await UserTester.signup_with_google()
    quiz = (await user_tester.create_quiz()).quiz

    response = await user_tester.get_next_quiz_question(quiz.token)
    assert response.quiz_question.question_name == HEIGHT_QUESTION_NAME
    assert response.quiz_question.display_question == HEIGHT_QUESTION_NAME
    assert response.quiz_question.token.startswith("qq_")

    assert len(response.available_answers) == 3
    assert response.available_answers[0].answer_name == 'Рост низкий'
    assert response.available_answers[0].display_answer == 'Рост низкий'
    assert response.available_answers[1].answer_name == 'Рост средний'
    assert response.available_answers[1].display_answer == 'Рост средний'
    assert response.available_answers[2].answer_name == 'Рост высокий'
    assert response.available_answers[2].display_answer == 'Рост высокий'

    with transaction() as session:
        db_quiz = QuizQuestionQueries.find_by_token(session, response.quiz_question.token)
        assert db_quiz.quiz.token == quiz.token
        assert db_quiz.token == response.quiz_question.token
        assert db_quiz.question_name == response.quiz_question.question_name
        assert db_quiz.quiz_step == QuizStep.STEP_1
        assert db_quiz.quiz_substep == QuizSubStep.STEP1_SUBSTEP_10
        assert db_quiz.followup_question_signs == []
        assert db_quiz.answer is None


# @pytest.mark.asyncio
# async def test_first_four_tablet_questions():
#     user_tester = await UserTester.signup_with_google()
#     quiz = (await user_tester.create_quiz()).quiz
#
#     quizzes = (await user_tester.get_quizzes()).quizzes
#     assert len(quizzes) == 1
#
#     await user_tester.delete_quiz(quiz.token)
#
#     quizzes_after_delete = (await user_tester.get_quizzes()).quizzes
#     assert quizzes_after_delete == []
#
#     with transaction() as session:
#         db_quiz = QuizQueries.find_by_token(session, quiz.token)
#         assert db_quiz.deleted_at == clock.now()
