import pytest

from common.clock import clock
from common.exceptions import BadRequest, Unauthorized
from database.db_quiz import DbQuiz
from database.quiz_queries import QuizQueries
from database.transaction import transaction
from tests.test_utils.user_tester import UserTester


def setup_module(module):
    print(f"Setting up for {module.__name__}")


@pytest.mark.asyncio
async def test_anonymous_user_can_create_quiz():
    with transaction() as session:
        existing_quizzes = session.query(DbQuiz).all()
        assert existing_quizzes == []

    anonymous_user_tester = await UserTester.visit()
    quiz = (await anonymous_user_tester.create_quiz()).quiz
    assert quiz.token.startswith("q_")
    assert quiz.user_token is None
    assert quiz.subject_name is None
    assert quiz.pronounce is None

    quizzes = (await anonymous_user_tester.get_quizzes()).quizzes
    assert len(quizzes) == 1
    assert quizzes[0].token == quiz.token

    with transaction() as session:
        all_quizzes = session.query(DbQuiz).all()
        assert len(all_quizzes) == 1

        db_quizzes = QuizQueries.find_all_by_logged_out_session_token(session, anonymous_user_tester.session_token)
        assert len(db_quizzes) == 1
        assert db_quizzes[0].session_token == anonymous_user_tester.session_token
        assert db_quizzes[0].user_id is None


@pytest.mark.asyncio
async def test_logged_in_user_can_create_quiz():
    with transaction() as session:
        existing_quizzes = session.query(DbQuiz).all()
        assert existing_quizzes == []

    user_tester = await UserTester.signup_with_google()
    quiz = (await user_tester.create_quiz()).quiz
    assert quiz.token.startswith("q_")
    assert quiz.user_token == user_tester.user.token
    assert quiz.subject_name is None
    assert quiz.pronounce is None

    quizzes = (await user_tester.get_quizzes()).quizzes
    assert len(quizzes) == 1
    assert quizzes[0].token == quiz.token

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
    user_tester = await UserTester.visit()
    await user_tester.create_quiz()

    quizzes = (await user_tester.get_quizzes()).quizzes
    assert len(quizzes) == 1
    assert quizzes[0].user_token is None

    await user_tester.login_with_google()
    logged_in_quizzes = (await user_tester.get_quizzes()).quizzes
    assert len(logged_in_quizzes) == 1
    assert logged_in_quizzes[0].user_token == user_tester.user.token
    assert logged_in_quizzes[0].token == quizzes[0].token


@pytest.mark.asyncio
async def test_when_anonymous_user_logs_in_quiz_ownership_is_not_transferred_from_owned_quizzes():
    logged_in_user_tester = await UserTester.signup_with_google("user@gmail.com")
    already_owned_quiz = (await logged_in_user_tester.create_quiz()).quiz
    assert already_owned_quiz.user_token == logged_in_user_tester.user.token

    user_tester = await UserTester.visit()
    quiz = (await user_tester.create_quiz()).quiz

    with transaction() as session:
        db_quiz = QuizQueries.find_all_by_user_token(session, logged_in_user_tester.user.token)[0]
        # Somehow the quiz has the same session token as another user. This can't really happen but just in case
        db_quiz.session_token = user_tester.session_token

    await user_tester.login_with_google("other.user@gmail.com")
    logged_in_quizzes = (await user_tester.get_quizzes()).quizzes
    assert len(logged_in_quizzes) == 1
    assert logged_in_quizzes[0].user_token == user_tester.user.token
    assert logged_in_quizzes[0].token == quiz.token


@pytest.mark.asyncio
async def test_anonymous_user_can_delete_quiz():
    anonymous_user_tester = await UserTester.visit()
    quiz = (await anonymous_user_tester.create_quiz()).quiz

    quizzes = (await anonymous_user_tester.get_quizzes()).quizzes
    assert len(quizzes) == 1

    await anonymous_user_tester.delete_quiz(quiz.token)

    quizzes_after_delete = (await anonymous_user_tester.get_quizzes()).quizzes
    assert quizzes_after_delete == []

    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, quiz.token)
        assert db_quiz.deleted_at == clock.now()


@pytest.mark.asyncio
async def test_logged_in_user_can_delete_quiz():
    user_tester = await UserTester.signup_with_google()
    quiz = (await user_tester.create_quiz()).quiz

    quizzes = (await user_tester.get_quizzes()).quizzes
    assert len(quizzes) == 1

    await user_tester.delete_quiz(quiz.token)

    quizzes_after_delete = (await user_tester.get_quizzes()).quizzes
    assert quizzes_after_delete == []

    with transaction() as session:
        db_quiz = QuizQueries.find_by_token(session, quiz.token)
        assert db_quiz.deleted_at == clock.now()


@pytest.mark.asyncio
async def test_logged_in_user_can_delete_their_quiz_from_another_session():
    user_tester = await UserTester.signup_with_google("user@gmail.com")
    quiz = (await user_tester.create_quiz()).quiz

    same_user_tester = await UserTester.signup_with_google("user@gmail.com")
    await same_user_tester.delete_quiz(quiz.token)

    quizzes_after_delete = (await same_user_tester.get_quizzes()).quizzes
    assert quizzes_after_delete == []


@pytest.mark.asyncio
async def test_cannot_delete_quiz_twice():
    user_tester = await UserTester.signup_with_google()
    quiz = (await user_tester.create_quiz()).quiz

    await user_tester.delete_quiz(quiz.token)

    with pytest.raises(BadRequest) as e:
        await user_tester.delete_quiz(quiz.token)
        assert "Cannot find quiz" in e.value.message


@pytest.mark.asyncio
async def test_logged_in_user_cannot_delete_other_logged_in_users_quiz():
    user_tester = await UserTester.signup_with_google("user@gmail.com")
    quiz = (await user_tester.create_quiz()).quiz

    user_tester2 = await UserTester.signup_with_google("other.user@gmail.com")

    with pytest.raises(Unauthorized) as e:
        await user_tester2.delete_quiz(quiz.token)
        assert "not allowed" in e.value.message


@pytest.mark.asyncio
async def test_anonymous_user_cannot_delete_other_anonymous_users_quiz():
    user_tester = await UserTester.visit()
    quiz = (await user_tester.create_quiz()).quiz

    user_tester2 = await UserTester.visit()

    with pytest.raises(Unauthorized) as e:
        await user_tester2.delete_quiz(quiz.token)
        assert "not allowed" in e.value.message


@pytest.mark.asyncio
async def test_anonymous_user_cannot_delete_other_anonymous_users_quiz():
    user_tester = await UserTester.visit()
    quiz = (await user_tester.create_quiz()).quiz

    user_tester2 = await UserTester.visit()

    with pytest.raises(Unauthorized) as e:
        await user_tester2.delete_quiz(quiz.token)
        assert "not allowed" in e.value.message
