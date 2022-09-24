from fastapi import Request

_test_instance = None


class TestGoogleOAuthService:
    email_address_to_return: str

    async def authorize_redirect(self, request: Request, redirect_uri: str):
        pass

    async def authorize_access_token_and_get_email_address(self, request: Request) -> str:
        return self.email_address_to_return


def get_test_google_oauth_service() -> TestGoogleOAuthService:
    # This way we emulate a singleton that is not created when module is imported unless this method is called
    global _test_instance
    if _test_instance is None:
        _test_instance = TestGoogleOAuthService()

    return _test_instance
