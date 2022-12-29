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

    # We don't have the dominant sign after step 1 yet because we calculate it when fetching next question
    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_1 is None

    # Dominant sign is WOOD, so we should get a followup question
    question5 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)

    # we now have the dominant sign for step 1
    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_1 == Sign.WOOD

    assert question5.quiz_question.question_name == QuestionName.NOSE_SHAPE
    assert question5.followup_question_signs == [Sign.WOOD, Sign.WOOD]
    assert question5.quiz_step == QuizStep.STEP_2
    assert question5.quiz_substep == QuizSubStep.STEP2_SUBSTEP_10_20
    answer5 = await user_tester.submit_quiz_answer(question5.quiz_question.token, 'Горбинка на носу')
    assert answer5.current_sign_scores == [-3, 1, 22, 25, 40]  # added [0, 0, 0, 0, 7]
    assert answer5.signs_for_next_questions == [Sign.WOOD, Sign.WOOD]

    # Still asking the remaining WOOD question
    question6 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question6.quiz_question.question_name == QuestionName.STRUCTURE_OF_HAIR
    assert question6.followup_question_signs == [Sign.WOOD]
    assert question6.quiz_step == QuizStep.STEP_2
    assert question6.quiz_substep == QuizSubStep.STEP2_SUBSTEP_10_20
    answer6 = await user_tester.submit_quiz_answer(question6.quiz_question.token, 'Прямые волосы')
    assert answer6.current_sign_scores == [-8, 9, 30, 25, 37]  # added [-5, 8, 8, 0, -3]
    assert answer6.signs_for_next_questions == [Sign.WOOD]

    # We don't have the dominant sign after step 2 yet because we calculate it when fetching next question
    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_2 is None

    question7 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)

    quiz_tester.refresh_from_db()
    assert quiz_tester.quiz.dm_after_step_2 == Sign.WOOD

    # Dm has changed so we are asking two questions for new Dm
    assert question7.quiz_question.question_name == QuestionName.BODY_FEATURES
    assert question7.followup_question_signs == [Sign.METAL, Sign.METAL]
    assert question7.quiz_step == QuizStep.STEP_3
    assert question7.quiz_substep == QuizSubStep.STEP3_SUBSTEP_10_20
    answer7 = await user_tester.submit_quiz_answer(question7.quiz_question.token, 'Затрудняюсь ответить')
    assert answer7.current_sign_scores == [-8, 9, 30, 25, 37]  # added [0, 0, 0, 0, 0] so stays the same
    assert answer7.signs_for_next_questions == [Sign.METAL, Sign.METAL]

    question8 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question8.quiz_question.question_name == QuestionName.BACK_OF_NOSE
    assert question8.followup_question_signs == [Sign.METAL, Sign.METAL]
    assert question8.quiz_step == QuizStep.STEP_3
    assert question8.quiz_substep == QuizSubStep.STEP3_SUBSTEP_10_20
    answer8 = await user_tester.submit_quiz_answer(question8.quiz_question.token, 'Длинная спинка носа')
    assert answer8.current_sign_scores == [-13, 6, 45, 25, 42]  # added [-5, -3, 15, 0, 5]
    assert answer8.signs_for_next_questions == [Sign.METAL, Sign.METAL]

    question9 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    assert question9.quiz_question.question_name == QuestionName.FACE_SHAPE
    assert question9.followup_question_signs == [Sign.METAL]
    assert question9.quiz_step == QuizStep.STEP_3
    assert question9.quiz_substep == QuizSubStep.STEP3_SUBSTEP_10_20
    answer9 = await user_tester.submit_quiz_answer(question9.quiz_question.token, 'Вытянутый прямоугольник')
    assert answer9.current_sign_scores == [-13, 6, 55, 25, 44]  # added [0, 0, 10, 0, 2]
    assert answer9.signs_for_next_questions == [Sign.METAL]

    # # We don't have the dominant sign after step 3 yet
    # quiz_tester.refresh_from_db()
    # assert quiz_tester.quiz.dm_after_step_3 is None
    #
    # question9 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    #
    # quiz_tester.refresh_from_db()
    # assert quiz_tester.quiz.dm_after_step_3 == Sign.EARTH
    #
    # # We are asking questions for Zn3
    # assert question9.quiz_question.question_name == QuestionName.HAIR_DENSITY
    # assert question9.followup_question_signs == [Sign.WATER]
    # assert question9.quiz_step == QuizStep.STEP_4
    # assert question9.quiz_substep == QuizSubStep.STEP4_SUBSTEP_10_20
    # answer9 = await user_tester.submit_quiz_answer(question9.quiz_question.token, 'Редкие волосы')
    # assert answer9.current_sign_scores == [-2, 37, 38, 18, 2]  # added [0, -3, 10, 0, 0]
    # assert answer9.signs_for_next_questions == [Sign.WATER]
    #
    # question10 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    # assert question10.quiz_question.question_name == QuestionName.NOSE_TIP
    # assert question10.followup_question_signs == []
    # assert question10.quiz_step == QuizStep.STEP_4
    # assert question10.quiz_substep == QuizSubStep.STEP4_SUBSTEP_10_20
    # answer10 = await user_tester.submit_quiz_answer(question10.quiz_question.token, 'Круглый кончик носа')
    # assert answer10.current_sign_scores == [-5, 42, 35, 23, 2]  # added [-3, 5, -3, 5, 0]
    # assert answer10.signs_for_next_questions == []
    #
    # # We don't have the dominant sign after step 4 yet
    # quiz_tester.refresh_from_db()
    # assert quiz_tester.quiz.dm_after_step_4 is None
    #
    # question11 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    #
    # quiz_tester.refresh_from_db()
    # assert quiz_tester.quiz.dm_after_step_4 == Sign.EARTH
    #
    # # Dm hasn't changed so we are asking questions for Dm, Zn2 и Zn3
    # assert question11.quiz_question.question_name == QuestionName.FACE_SHAPE
    # assert question11.quiz_step == QuizStep.STEP_5
    # assert question11.quiz_substep == QuizSubStep.STEP5_SUBSTEP_10_20_30
    # assert question11.followup_question_signs == [Sign.METAL, Sign.WATER]
    # answer11 = await user_tester.submit_quiz_answer(question11.quiz_question.token, 'Широк прямоугольн "Квадрат"')
    # assert answer11.current_sign_scores == [-7, 42, 35, 30, 2]  # added [-2, 0, 0, 7, 0]
    # assert answer11.signs_for_next_questions == [Sign.METAL, Sign.WATER]
    #
    # question12 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    # assert question12.quiz_question.question_name == QuestionName.BACK_OF_NOSE
    # assert question12.quiz_step == QuizStep.STEP_5
    # assert question12.quiz_substep == QuizSubStep.STEP5_SUBSTEP_10_20_30
    # assert question12.followup_question_signs == [Sign.WATER]
    # answer12 = await user_tester.submit_quiz_answer(question12.quiz_question.token, 'Длинная спинка носа')
    # assert answer12.current_sign_scores == [-12, 39, 50, 30, 7]  # added [-5, -3, 15, 0, 5]
    # assert answer12.signs_for_next_questions == [Sign.WATER]
    #
    # question13 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    # assert question13.quiz_question.question_name == QuestionName.HAIR_FEATURES
    # assert question13.quiz_step == QuizStep.STEP_5
    # assert question13.quiz_substep == QuizSubStep.STEP5_SUBSTEP_10_20_30
    # assert question13.followup_question_signs == []
    # answer13 = await user_tester.submit_quiz_answer(question13.quiz_question.token, 'Ранние залысины')
    # assert answer13.current_sign_scores == [-12, 39, 53, 35, 7]  # added [0, 0, 3, 5, 0]
    # assert answer13.signs_for_next_questions == []
    #
    # # Last three questions in step 6
    # question14 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    # assert question14.quiz_question.question_name == QuestionName.NOSE_SHAPE
    # assert question14.quiz_step == QuizStep.STEP_6
    # assert question14.quiz_substep == QuizSubStep.STEP6_SUBSTEP_10_20_30
    # assert question14.followup_question_signs == [Sign.EARTH, Sign.WATER]
    # answer14 = await user_tester.submit_quiz_answer(question14.quiz_question.token, 'Горбинка на носу')
    # assert answer14.current_sign_scores == [-12, 39, 53, 35, 14]  # added [0, 0, 0, 0, 7]
    # assert answer14.signs_for_next_questions == [Sign.EARTH, Sign.WATER]
    #
    # question15 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    # assert question15.quiz_question.question_name == QuestionName.WIDTH_OF_BACK_OF_NOSE
    # assert question15.quiz_step == QuizStep.STEP_6
    # assert question15.quiz_substep == QuizSubStep.STEP6_SUBSTEP_10_20_30
    # assert question15.followup_question_signs == [Sign.WATER]
    # answer15 = await user_tester.submit_quiz_answer(question15.quiz_question.token, 'Затрудняюсь ответить')
    # assert answer15.current_sign_scores == [-12, 39, 53, 35, 14]  # added [0, 0, 0, 0, 0] so stays the same
    # assert answer15.signs_for_next_questions == [Sign.WATER]
    #
    # question16 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    # assert question16.quiz_question.question_name == QuestionName.FAT_TISSUE
    # assert question16.quiz_step == QuizStep.STEP_6
    # assert question16.quiz_substep == QuizSubStep.STEP6_SUBSTEP_10_20_30
    # assert question16.followup_question_signs == []
    # answer16 = await user_tester.submit_quiz_answer(question16.quiz_question.token, 'Затрудняюсь ответить')
    # assert answer16.current_sign_scores == [-12, 39, 53, 35, 14]  # added [0, 0, 0, 0, 0] so stays the same
    # assert answer16.signs_for_next_questions == []
    #
    # question17 = await user_tester.get_next_quiz_question(quiz_tester.quiz.token)
    # assert question17.quiz_question is None
    # assert question17.available_answers == []
    #
    # await user_tester.update_quiz(quiz_tester.quiz.token, subject_name='Снежана', pronounce=Pronounce.SHE_HER)
    # # response = await user_tester.generate_quiz_summary(quiz_tester.quiz.token)
    # # assert response.summaries is not None
