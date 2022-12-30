import pytest

from models.pronounce import Pronounce
from models.sign import Sign
from quizzes.question_database import QuestionName
from quizzes.quiz_steps import QuizStep, QuizSubStep
from tests.test_utils.user_tester import UserTester


@pytest.mark.asyncio
async def test_021223_1_3_1():
    user_tester = await UserTester.signup_with_google()
    quiz_tester = await user_tester.create_quiz()

    question1 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question1.quiz_question.question_name == QuestionName.HEIGHT
    answer1 = await user_tester.submit_quiz_answer(question1.quiz_question.token, 'Рост высокий')
    assert answer1.current_sign_scores == [-5, -3, 15, 8, 10]

    question2 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question2.quiz_question.question_name == QuestionName.BODY_SCHEME
    answer2 = await user_tester.submit_quiz_answer(question2.quiz_question.token, 'Шире в плечах')
    assert answer2.current_sign_scores == [-5, -6, 15, 15, 25]  # added [0, -3, 0, 7, 10]

    question3 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question3.quiz_question.question_name == QuestionName.EYE_COLOR
    answer3 = await user_tester.submit_quiz_answer(question3.quiz_question.token, 'Серо-голуб гл с темн вкрапл')
    assert answer3.current_sign_scores == [-3, 1, 22, 15, 28]  # added [0, 0, 0, 0, 3]

    question4 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question4.quiz_question.question_name == QuestionName.HAIR_COLOR
    answer4 = await user_tester.submit_quiz_answer(question4.quiz_question.token, 'Русые волосы')
    assert answer4.current_sign_scores == [-3, 1, 22, 25, 33]  # added [0, 0, 0, 10, 5]

    # We don't have the dominant sign after this step yet because we calculate it when fetching next question
    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_1 is None

    # We have dominant sign for this step now; we can re-fetch the same question later
    await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_1 == Sign.WOOD

    question5 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question5.quiz_substep == QuizSubStep.STEP2_SUBSTEP_10_20
    assert question5.quiz_question.question_name == QuestionName.NOSE_SHAPE
    assert question5.followup_question_signs == [Sign.WOOD, Sign.WOOD]
    assert question5.quiz_step == QuizStep.STEP_2
    answer5 = await user_tester.submit_quiz_answer(question5.quiz_question.token, 'Горбинка на носу')
    assert answer5.current_sign_scores == [-3, 1, 22, 25, 40]  # added [0, 0, 0, 0, 7]
    assert answer5.signs_for_next_questions == [Sign.WOOD, Sign.WOOD]

    question6 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question6.quiz_substep == QuizSubStep.STEP2_SUBSTEP_10_20
    assert question6.quiz_question.question_name == QuestionName.STRUCTURE_OF_HAIR
    assert question6.followup_question_signs == [Sign.WOOD]
    assert question6.quiz_step == QuizStep.STEP_2
    answer6 = await user_tester.submit_quiz_answer(question6.quiz_question.token, 'Прямые волосы')
    assert answer6.current_sign_scores == [-8, 9, 30, 25, 37]  # added [-5, 8, 8, 0, -3]
    assert answer6.signs_for_next_questions == [Sign.WOOD]

    # We don't have the dominant sign after this step yet because we calculate it when fetching next question
    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_2 is None

    # We have dominant sign for this step now; we can re-fetch the same question later
    await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_2 == Sign.WOOD

    question7 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question7.quiz_substep == QuizSubStep.STEP3_SUBSTEP_10_20
    assert question7.quiz_question.question_name == QuestionName.BODY_FEATURES
    assert question7.followup_question_signs == [Sign.METAL, Sign.METAL]
    assert question7.quiz_step == QuizStep.STEP_3
    answer7 = await user_tester.submit_quiz_answer(question7.quiz_question.token, 'Затрудняюсь ответить')
    assert answer7.current_sign_scores == [-8, 9, 30, 25, 37]  # added [0, 0, 0, 0, 0] so stays the same
    assert answer7.signs_for_next_questions == [Sign.METAL, Sign.METAL]

    question8 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question8.quiz_substep == QuizSubStep.STEP3_SUBSTEP_10_20
    assert question8.quiz_question.question_name == QuestionName.BACK_OF_NOSE
    assert question8.followup_question_signs == [Sign.METAL, Sign.METAL]
    assert question8.quiz_step == QuizStep.STEP_3
    answer8 = await user_tester.submit_quiz_answer(question8.quiz_question.token, 'Длинная спинка носа')
    assert answer8.current_sign_scores == [-13, 6, 45, 25, 42]  # added [-5, -3, 15, 0, 5]
    assert answer8.signs_for_next_questions == [Sign.METAL, Sign.METAL]

    question9 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question9.quiz_substep == QuizSubStep.STEP3_SUBSTEP_10_20
    assert question9.quiz_question.question_name == QuestionName.FACE_SHAPE
    assert question9.followup_question_signs == [Sign.METAL]
    assert question9.quiz_step == QuizStep.STEP_3
    answer9 = await user_tester.submit_quiz_answer(question9.quiz_question.token, 'Вытянутый прямоугольник')
    assert answer9.current_sign_scores == [-13, 6, 55, 25, 44]  # added [0, 0, 10, 0, 2]
    assert answer9.signs_for_next_questions == [Sign.METAL]

    # We don't have the dominant sign after this step yet because we calculate it when fetching next question
    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_3 is None

    # We have dominant sign for this step now; we can re-fetch the same question later
    await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_3 == Sign.METAL

    question10 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question10.quiz_substep == QuizSubStep.STEP4_SUBSTEP_50_60
    assert question10.quiz_question.question_name == QuestionName.THICKNESS_OF_HAIR
    assert question10.followup_question_signs == [Sign.METAL, Sign.METAL]
    assert question10.quiz_step == QuizStep.STEP_4
    answer10 = await user_tester.submit_quiz_answer(question10.quiz_question.token, 'Волосы средней толщины')
    assert answer10.current_sign_scores == [-13, 6, 55, 25, 44]  # added [0, 0, 0, 0, 0] so stays the same
    assert answer10.signs_for_next_questions == [Sign.METAL, Sign.METAL]

    question11 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question11.quiz_substep == QuizSubStep.STEP4_SUBSTEP_50_60
    assert question11.quiz_question.question_name == QuestionName.HAIR_DENSITY
    assert question11.followup_question_signs == [Sign.METAL, Sign.METAL]
    assert question11.quiz_step == QuizStep.STEP_4
    answer11 = await user_tester.submit_quiz_answer(question11.quiz_question.token, 'Затрудняюсь ответить')
    assert answer11.current_sign_scores == [-13, 6, 55, 25, 44]  # added [0, 0, 0, 0, 0] so stays the same
    assert answer11.signs_for_next_questions == [Sign.METAL, Sign.METAL]

    #
    # question17 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    # assert question17.quiz_question is None
    # assert question17.available_answers == []
    #
    # await user_tester.update_quiz(quiz_tester.quiz.token, subject_name='Снежана', pronounce=Pronounce.SHE_HER)
    # # response = await user_tester.generate_quiz_summary(quiz_tester.quiz.token)
    # # assert response.summaries is not None
