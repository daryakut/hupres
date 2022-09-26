from typing import Optional

from pydantic import BaseModel

from database.db_quiz import DbQuiz
from quizzes.models import UserRole


class SessionData(BaseModel):
    created_at: str
    session_token: str
    user_token: Optional[str]
    user_role: Optional[UserRole]

    def is_admin(self) -> bool:
        return self.user_role == UserRole.ADMIN

    def is_admin_or_owner_of(self, db_quiz: DbQuiz) -> bool:
        if self.is_admin():
            return True

        if self.user_token is not None:
            return db_quiz.user.token == self.user_token

        return db_quiz.session_token == self.session_token
