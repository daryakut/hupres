from typing import Optional

from common.clock import clock
from models.token import generate_session_token
from quizzes.models import UserRole
from users.session_data import SessionData

_fake_instance = None


class FakeSessionDataProvider:
    session_data: Optional[SessionData] = None

    def initialize_session(self) -> SessionData:
        self.session_data = SessionData(
            created_at=clock.now_ms(),
            session_token=generate_session_token(),
        )
        print(f"INITIALIZED SESSION {self.session_data.session_token}")
        return self.session_data

    def get_current_session(self) -> SessionData:
        return self.session_data

    def update_current_session(self, user_token: Optional[str], user_role: Optional[UserRole]):
        print(f"Logging in user {user_token}, {self.session_data.session_token}")
        self.session_data.user_token = user_token
        self.session_data.user_role = user_role


def get_fake_session_data_provider() -> FakeSessionDataProvider:
    # This way we emulate a singleton that is not created when module is imported unless this method is called
    global _fake_instance
    if _fake_instance is None:
        _fake_instance = FakeSessionDataProvider()

    return _fake_instance
