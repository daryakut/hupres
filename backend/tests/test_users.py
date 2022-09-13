import pytest

from app import user_signup, UserSignupRequest


class UsersTest:
    def setup_module(self, method):
        print(f"Setting up for {method.__name__}")

    @pytest.mark.asyncio
    async def test_can_create_user(self):
        response = await user_signup(UserSignupRequest(email_address="georgii@hupres.com"))
        assert response.user.email_address == "georgii@hupres.com"
