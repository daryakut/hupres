import pytest

from common.clock import clock
from common.exceptions import BadRequest, Unauthorized
from database.db_quiz import DbQuiz
from database.quiz_answer_queries import QuizAnswerQueries
from database.quiz_queries import QuizQueries
from database.quiz_question_queries import QuizQuestionQueries
from database.transaction import transaction
from quizzes.constants import QuizStep, QuizSubStep
from quizzes.question_database import QuestionName
from tests.test_utils.user_tester import UserTester


def setup_module(module):
    print(f"Setting up for {module.__name__}")


@pytest.mark.asyncio
async def test_can_get_first_question():
    user_tester = await UserTester.signup_with_google()
    quiz = (await user_tester.create_quiz()).quiz

    question_tester = await user_tester.get_next_quiz_question(quiz.token)
    assert question_tester.quiz_question.question_name == QuestionName.HEIGHT
    assert question_tester.quiz_question.question_display_name == 'Рост'

    assert len(question_tester.available_answers) == 3
    assert question_tester.available_answers[0].answer_name == 'Рост низкий'
    assert question_tester.available_answers[0].display_answer == 'Рост низкий'
    assert question_tester.available_answers[1].answer_name == 'Рост средний'
    assert question_tester.available_answers[1].display_answer == 'Рост средний'
    assert question_tester.available_answers[2].answer_name == 'Рост высокий'
    assert question_tester.available_answers[2].display_answer == 'Рост высокий'

    assert question_tester.question_name == question_tester.quiz_question.question_name
    assert question_tester.quiz_step == QuizStep.STEP_1
    assert question_tester.quiz_substep == QuizSubStep.STEP1_SUBSTEP_10
    assert question_tester.followup_question_signs == []
    assert question_tester.answer_token is None

    # Re-fetching the same question does not re-created it
    question_tester2 = await user_tester.get_next_quiz_question(quiz.token)
    assert question_tester2.quiz_question.question_name == QuestionName.HEIGHT
    assert question_tester2.quiz_question.token == question_tester.quiz_question.token


@pytest.mark.asyncio
async def test_can_respond_to_first_question():
    user_tester = await UserTester.signup_with_google()
    quiz = (await user_tester.create_quiz()).quiz

    question_tester = await user_tester.get_next_quiz_question(quiz.token)
    assert question_tester.quiz_question.question_name == QuestionName.HEIGHT
    assert question_tester.available_answers[0].answer_name == 'Рост низкий'

    answer_tester = await user_tester.submit_quiz_answer(question_tester.quiz_question.token, 'Рост низкий')
    assert answer_tester.quiz_token == quiz.token
    assert answer_tester.answer_name == 'Рост низкий'
    assert answer_tester.is_all_zeros is False
    assert answer_tester.current_sign_scores == [15, 6, -5, -3, -3]
    assert answer_tester.original_sign_scores == []
    assert answer_tester.signs_for_next_questions == []


@pytest.mark.asyncio
async def test_cannot_get_other_users_question():
    user_tester = await UserTester.signup_with_google("user@gmail.com")
    quiz = (await user_tester.create_quiz()).quiz

    user_tester2 = await UserTester.signup_with_google("other.user@gmail.com")

    with pytest.raises(Unauthorized) as e:
        await user_tester2.get_next_quiz_question(quiz.token)
    assert "not allowed" in str(e.value)


@pytest.mark.asyncio
async def test_cannot_respond_to_same_question_twice():
    user_tester = await UserTester.signup_with_google()
    quiz = (await user_tester.create_quiz()).quiz

    question_tester = await user_tester.get_next_quiz_question(quiz.token)
    assert question_tester.quiz_question.question_name == QuestionName.HEIGHT

    await user_tester.submit_quiz_answer(question_tester.quiz_question.token, 'Рост низкий')
    with pytest.raises(ValueError) as e:
        await user_tester.submit_quiz_answer(question_tester.quiz_question.token, 'Рост низкий')
    assert "You have already responded to question" in str(e.value)


@pytest.mark.asyncio
async def test_cannot_respond_to_other_users_question():
    user_tester = await UserTester.signup_with_google("user@gmail.com")
    quiz = (await user_tester.create_quiz()).quiz
    quiestion_tester = await user_tester.get_next_quiz_question(quiz.token)
    assert quiestion_tester.quiz_question.question_name == QuestionName.HEIGHT

    user_tester2 = await UserTester.signup_with_google("other.user@gmail.com")

    with pytest.raises(Unauthorized) as e:
        await user_tester2.submit_quiz_answer(quiestion_tester.quiz_question.token, 'Рост низкий')
    assert "not allowed" in str(e.value)


@pytest.mark.asyncio
async def test_can_get_first_four_tablet_questions():
    user_tester = await UserTester.signup_with_google()
    quiz = (await user_tester.create_quiz()).quiz

    question1 = await user_tester.get_next_quiz_question(quiz.token)
    assert question1.quiz_question.question_name == QuestionName.HEIGHT
    assert question1.quiz_step == QuizStep.STEP_1
    assert question1.quiz_substep == QuizSubStep.STEP1_SUBSTEP_10
    assert question1.followup_question_signs == []
    assert question1.answer is None
    answer1 = await user_tester.submit_quiz_answer(question1.quiz_question.token, 'Рост низкий')
    assert answer1.answer_name == 'Рост низкий'
    assert answer1.is_all_zeros is False
    assert answer1.current_sign_scores == [15, 6, -5, -3, -3]
    assert answer1.original_sign_scores == []
    assert answer1.signs_for_next_questions == []

    question2 = await user_tester.get_next_quiz_question(quiz.token)
    assert question2.quiz_question.question_name == QuestionName.BODY_SCHEME
    assert question2.quiz_step == QuizStep.STEP_1
    assert question2.quiz_substep == QuizSubStep.STEP1_SUBSTEP_20
    assert question2.followup_question_signs == []
    assert question2.answer is None
    answer2 = await user_tester.submit_quiz_answer(question1.quiz_question.token, 'Малый прямоугольник')
    assert answer2.answer_name == 'Малый прямоугольник'
    assert answer2.is_all_zeros is False
    assert answer2.current_sign_scores == [15, 6, -5, -3, -3]
    assert answer2.original_sign_scores == []
    assert answer2.signs_for_next_questions == []

    response2 = await user_tester.get_next_quiz_question(quiz.token)
    assert response2.quiz_question.question_name == QuestionName.BODY_SCHEME
    answer2_token = await user_tester.submit_quiz_answer(question1.quiz_question.token, 'Малый прямоугольник')
    with transaction() as session:
        db_answer = QuizAnswerQueries.find_by_token(session, answer2_token)
        assert db_answer.answer_name == 'Рост низкий'
        assert db_answer.is_all_zeros is False
        assert db_answer.current_sign_scores == [15, 6, -5, -3, -3]
        assert db_answer.signs_for_next_questions == []

    assert len(question1.available_answers) == 3
    assert question1.available_answers[0].answer_name == 'Рост низкий'
    assert question1.available_answers[0].display_answer == 'Рост низкий'
    assert question1.available_answers[1].answer_name == 'Рост средний'
    assert question1.available_answers[1].display_answer == 'Рост средний'
    assert question1.available_answers[2].answer_name == 'Рост высокий'
    assert question1.available_answers[2].display_answer == 'Рост высокий'

    with transaction() as session:
        db_question = QuizQuestionQueries.find_by_token(session, response.quiz_question.token)
        assert db_question.quiz.token.value == quiz.token
        assert db_question.token.value == response.quiz_question.token
        assert db_question.question_name == response.quiz_question.question_name
        assert db_question.quiz_step == QuizStep.STEP_1
        assert db_question.quiz_substep == QuizSubStep.STEP1_SUBSTEP_10
        assert db_question.followup_question_signs == []
        assert db_question.answer is None

    # Re-fetching the same question does not re-created it
    response2 = await user_tester.get_next_quiz_question(quiz.token)
    assert response2.quiz_question.question_name == QuestionName.HEIGHT
    assert response2.quiz_question.token == response.quiz_question.token



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
