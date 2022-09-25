import pytest

from database.db_quiz import DbQuiz
from database.db_user import DbUser
from database.quiz_queries import QuizQueries, find_all_by_session_token
from database.transaction import transaction
from quizzes.models import UserRole
from tests.test_utils.user_tester import UserTester


def setup_module(module):
    print(f"Setting up for {module.__name__}")


@pytest.mark.asyncio
async def test_anonymous_user_can_create_quiz():
    with transaction() as session:
        existing_quizzes = session.query(DbQuiz).all()
        assert existing_quizzes == []

    anonymous_user_tester = UserTester.visit()
    await anonymous_user_tester.create_quiz()

    quizzes = (await anonymous_user_tester.get_quizzes()).quizzes
    assert len(quizzes) == 1
    assert quizzes[0].user_token is None
    assert quizzes[0].subject_name is None
    assert quizzes[0].pronounce is None
    assert quizzes[0].dm_after_step_1 is None
    assert quizzes[0].dm_after_step_2 is None
    assert quizzes[0].dm_after_step_3 is None
    assert quizzes[0].dm_after_step_4 is None

    with transaction() as session:
        all_quizzes = session.query(DbQuiz).all()
        assert len(all_quizzes) == 1

        db_quizzes = QuizQueries.find_all_by_session_token(session, anonymous_user_tester.session_token)
        assert len(db_quizzes) == 1
        assert db_quizzes[0].session_token == anonymous_user_tester.session_token
        assert db_quizzes[0].user_id is None


@pytest.mark.asyncio
async def test_logged_in_user_can_create_quiz():
    with transaction() as session:
        existing_quizzes = session.query(DbQuiz).all()
        assert existing_quizzes == []

    user_tester = await UserTester.signup_with_google()
    await user_tester.create_quiz()

    quizzes = (await user_tester.get_quizzes()).quizzes
    assert len(quizzes) == 1
    assert quizzes[0].user_token == user_tester.user.token
    assert quizzes[0].subject_name is None
    assert quizzes[0].pronounce is None
    assert quizzes[0].dm_after_step_1 is None
    assert quizzes[0].dm_after_step_2 is None
    assert quizzes[0].dm_after_step_3 is None
    assert quizzes[0].dm_after_step_4 is None

    with transaction() as session:
        all_quizzes = session.query(DbQuiz).all()
        assert len(all_quizzes) == 1

        db_quizzes = QuizQueries.find_all_by_user_token(session, user_tester.user.token)
        assert len(db_quizzes) == 1
        assert db_quizzes[0].session_token == user_tester.session_token
        assert db_quizzes[0].user_id is not None
        assert db_quizzes[0].user.token == user_tester.user.token


@pytest.mark.asyncio
async def test_when_anonymous_user_logs_in_quiz_ownership_is_transferred():
    pass
    # anonymous_user_tester = await UserTester.visit()
    # await anonymous_user_tester.create_quiz()
    #
    #
    # with transaction() as session:
    #     existing_quizzes = session.query(DbQuiz).all()
    #     assert existing_quizzes == []
    #
    # user_tester = await UserTester.signup_with_google()
    # await user_tester.create_quiz()
    #
    # quizzes = (await user_tester.get_quizzes()).quizzes
    # assert len(quizzes) == 1
    # assert quizzes[0].user_token == user_tester.user.token
    # assert quizzes[0].subject_name is None
    # assert quizzes[0].pronounce is None
    # assert quizzes[0].dm_after_step_1 is None
    # assert quizzes[0].dm_after_step_2 is None
    # assert quizzes[0].dm_after_step_3 is None
    # assert quizzes[0].dm_after_step_4 is None
    #
    # with transaction() as session:
    #     all_quizzes = session.query(DbQuiz).all()
    #     assert len(all_quizzes) == 1
    #
    #     db_quizzes = QuizQueries.find_all_by_user_token(session, user_tester.user.token)
    #     assert len(db_quizzes) == 1
    #     assert db_quizzes[0].session_token == user_tester.session_token
    #     assert db_quizzes[0].user_id is not None
    #     assert db_quizzes[0].user.token == user_tester.user.token
