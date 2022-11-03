import pytest

from quizzes.question_database import QuestionName
from tests.test_utils.user_tester import UserTester


@pytest.mark.asyncio
async def test_snizhana():
    user_tester = await UserTester.signup_with_google()
    quiz_tester = await user_tester.create_quiz()

    question1 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question1.quiz_question.question_name == QuestionName.HEIGHT
    answer1 = await user_tester.submit_quiz_answer(question1.quiz_question.token, 'Рост высокий')
    assert answer1.current_sign_scores == [-5, -3, 15, 8, 10]

    question2 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question2.quiz_question.question_name == QuestionName.BODY_SCHEME
    answer2 = await user_tester.submit_quiz_answer(question2.quiz_question.token, 'Шире в бедрах')
    assert answer2.current_sign_scores == [-5, 12, 8, 13, 5]  # added [0, 15, -7, 5, -5]

    question3 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question3.quiz_question.question_name == QuestionName.EYE_COLOR
    answer3 = await user_tester.submit_quiz_answer(question3.quiz_question.token, 'Рябые глаза')
    assert answer3.current_sign_scores == [-5, 10, 5, 13, 15]  # added [0, -2, -3, 0, 10]

    question4 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question4.quiz_question.question_name == QuestionName.HAIR_COLOR
    answer4 = await user_tester.submit_quiz_answer(question4.quiz_question.token, 'Русые волосы')
    assert answer4.current_sign_scores == [-5, 10, 5, 23, 20]  # added [0, 0, 0, 10, 5]

    question5 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)

