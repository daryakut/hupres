import pytest

from common.exceptions import Unauthorized
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
    assert question1.answer_token is None
    assert set(a.answer_name for a in question1.available_answers) == {
        'Рост низкий',
        'Рост средний',
        'Рост высокий',
    }

    answer1 = await user_tester.submit_quiz_answer(question1.quiz_question.token, 'Рост низкий')
    assert answer1.answer_name == 'Рост низкий'
    assert answer1.is_all_zeros is False
    assert answer1.current_sign_scores == [15, 6, -5, -3, -3]
    assert answer1.original_sign_scores == []
    assert answer1.signs_for_next_questions == []
    question1.refresh_from_db()
    assert question1.answer_token == answer1.quiz_answer_token

    question2 = await user_tester.get_next_quiz_question(quiz.token)
    assert question2.quiz_question.question_name == QuestionName.BODY_SCHEME
    assert question2.quiz_step == QuizStep.STEP_1
    assert question2.quiz_substep == QuizSubStep.STEP1_SUBSTEP_20
    assert question2.followup_question_signs == []
    assert question2.answer_token is None
    assert set(a.answer_name for a in question2.available_answers) == {
        'Малый прямоугольник',
        'Узкий прямоугольник',
        'Больш шир прямоугольник',
        'Шире в плечах',
        'Шире в бедрах',
        'Затрудняюсь ответить',
    }
    # Re-fetching the same question does not re-created it
    question2_refetched = await user_tester.get_next_quiz_question(quiz.token)
    assert question2_refetched.quiz_question.question_name == QuestionName.BODY_SCHEME
    assert question2_refetched.quiz_question.token == question2.quiz_question.token
    answer2 = await user_tester.submit_quiz_answer(question2.quiz_question.token, 'Малый прямоугольник')
    assert answer2.answer_name == 'Малый прямоугольник'
    assert answer2.is_all_zeros is False
    assert answer2.current_sign_scores == [30, 6, -5, -8, -8]  # added [15, 0, 0, -5, -5]
    assert answer2.original_sign_scores == []
    assert answer2.signs_for_next_questions == []
    question2.refresh_from_db()
    assert question2.answer_token == answer2.quiz_answer_token

    question3 = await user_tester.get_next_quiz_question(quiz.token)
    assert question3.quiz_question.question_name == QuestionName.EYE_COLOR
    assert question3.quiz_step == QuizStep.STEP_1
    assert question3.quiz_substep == QuizSubStep.STEP1_SUBSTEP_30
    assert question3.followup_question_signs == []
    assert question3.answer_token is None
    assert set(a.answer_name for a in question3.available_answers) == {
        'Голубые глаза',
        'Серые (стальные) глаза',
        'Серо-голуб гл с темн вкрапл',
        'Серо-голуб гл с жел-зел зонами',
        'Черные глаза',
        'Карие глаза',
        'Зеленые глаза',
        'Желто-зеленые глаза',
        'Рябые глаза',
        'Затрудняюсь ответить',
    }
    # Re-fetching the same question does not re-created it
    question3_refetched = await user_tester.get_next_quiz_question(quiz.token)
    assert question3_refetched.quiz_question.question_name == QuestionName.EYE_COLOR
    assert question3_refetched.quiz_question.token == question3.quiz_question.token
    answer3 = await user_tester.submit_quiz_answer(question3.quiz_question.token, 'Затрудняюсь ответить')
    assert answer3.answer_name == 'Затрудняюсь ответить'
    assert answer3.is_all_zeros is True
    assert answer3.current_sign_scores == [30, 6, -5, -8, -8]  # same as before as all were 0
    assert answer3.original_sign_scores == []
    assert answer3.signs_for_next_questions == []
    question3.refresh_from_db()
    assert question3.answer_token == answer3.quiz_answer_token

    question4 = await user_tester.get_next_quiz_question(quiz.token)
    assert question4.quiz_question.question_name == QuestionName.HAIR_COLOR
    assert question4.quiz_step == QuizStep.STEP_1
    assert question4.quiz_substep == QuizSubStep.STEP1_SUBSTEP_40
    assert question4.followup_question_signs == []
    assert question4.answer_token is None
    assert set(a.answer_name for a in question4.available_answers) == {
        'Рыжие волосы',
        'Каштановые волосы',
        'Черные волосы',
        'Темно русые волосы',
        'Русые волосы',
        'Светлые волосы',
        'Затрудняюсь ответить',
    }
    # Re-fetching the same question does not re-created it
    question4_refetched = await user_tester.get_next_quiz_question(quiz.token)
    assert question4_refetched.quiz_question.question_name == QuestionName.HAIR_COLOR
    assert question4_refetched.quiz_question.token == question4.quiz_question.token
    answer4 = await user_tester.submit_quiz_answer(question4.quiz_question.token, 'Русые волосы')
    assert answer4.answer_name == 'Русые волосы'
    assert answer4.is_all_zeros is False
    assert answer4.current_sign_scores == [30, 6, -5, 2, -3]  # added [0, 0, 0, 10, 5]
    assert answer4.original_sign_scores == []
    assert answer4.signs_for_next_questions == []
    question4.refresh_from_db()
    assert question4.answer_token == answer4.quiz_answer_token

