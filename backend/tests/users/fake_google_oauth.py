from fastapi import Request

from tests.users.fake_sessions import get_fake_session_data_provider

_fake_instance = None


class FakeGoogleOAuthService:
    email_address_to_return: str

    async def authorize_redirect(self, request: Request, redirect_uri: str):
        pass

    async def authorize_access_token_and_get_email_address(self, request: Request) -> str:
        return self.email_address_to_return


def get_fake_google_oauth_service() -> FakeGoogleOAuthService:
    # This way we emulate a singleton that is not created when module is imported unless this method is called
    global _fake_instance
    if _fake_instance is None:
        _fake_instance = FakeGoogleOAuthService()

    return _fake_instance
