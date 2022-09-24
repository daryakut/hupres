from typing import Optional

from common import clock
from users.session_data import SessionData

_test_instance = None


class TestSessionDataProvider:
    session_data: Optional[SessionData] = None

    def get_current_session(self) -> SessionData:
        return self.session_data

    def initialize_session(self):
        self.session_data = SessionData(
            created_at=clock.now_ms(),
        )

    def update_current_session(self, user_token: str):
        self.session_data.user_token = user_token


def get_test_session_data_provider() -> TestSessionDataProvider:
    # This way we emulate a singleton that is not created when module is imported unless this method is called
    global _test_instance
    if _test_instance is None:
        _test_instance = TestSessionDataProvider()

    return _test_instance
