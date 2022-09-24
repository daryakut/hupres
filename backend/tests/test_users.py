import pytest

from database.db_models import DbUser
from database.transaction import transaction
from quiz_algorithm.models import UserRole
from tests.test_utils.UserTester import UserTester


def setup_module(module):
    print(f"Setting up for {module.__name__}")


@pytest.mark.asyncio
async def test_can_create_user():
    user_tester = await UserTester.login_with_google(email_address="georgii@hupres.com")
    assert user_tester.user.email_address == "georgii@hupres.com"
    assert user_tester.user.role == UserRole.RESPONDENT


@pytest.mark.asyncio
async def test_can_create_admin_user():
    with transaction() as session:
        existing_users = session.query(DbUser).all()
        assert existing_users == []

    admin_user_tester = await UserTester.login_with_google(email_address="olgeorge.acc@gmail.com")
    assert admin_user_tester.user.email_address == "olgeorgeacc@gmail.com"
    assert admin_user_tester.user.role == UserRole.ADMIN


@pytest.mark.asyncio
async def test_does_not_create_multiple_users_with_same_email():
    admin_user_tester = await UserTester.login_with_google(email_address="user@gmail.com")
    assert admin_user_tester.user.email_address == "user@gmail.com"

    admin_user_tester2 = await UserTester.login_with_google(email_address="user@gmail.com")
    assert admin_user_tester2.user.email_address == "user@gmail.com"
    assert admin_user_tester2.user.token == admin_user_tester.user.token


@pytest.mark.asyncio
async def test_sanitizes_user_email_address():
    admin_user_tester = await UserTester.login_with_google(email_address="user+134@gmail.com")
    assert admin_user_tester.user.email_address == "user@gmail.com"

    admin_user_tester2 = await UserTester.login_with_google(email_address="u.s.e.r@gmail.com")
    assert admin_user_tester2.user.email_address == "user@gmail.com"

    assert admin_user_tester2.user.token == admin_user_tester.user.token
