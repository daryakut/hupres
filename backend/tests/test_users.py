import pytest

from tests.test_utils.UserTester import UserTester


def setup_module(module):
    print(f"Setting up for {module.__name__}")


@pytest.mark.asyncio
async def test_can_create_user():
    await UserTester.login_with_google()
    # user_tester = await UserTester.signup()
    # assert user_tester.user.email_address == "georgii@hupres.com"

    # response = await user_signup(UserSignupRequest(email_address="georgii@hupres.com"))
    # assert response.user.email_address == "georgii@hupres.com"
    # assert 3 + 3 == 6
