from typing import Optional

from pydantic import BaseModel

from database.db_quiz import DbQuiz
from models.token import Token
from quizzes.models import UserRole, User


class SessionData(BaseModel):
    created_at: str
    session_token: str
    user_token: Optional[Token[User]]
    user_role: Optional[UserRole]

    def is_admin(self) -> bool:
        return self.user_role == UserRole.ADMIN

    def is_owner_of(self, db_quiz: DbQuiz) -> bool:
        if self.user_token is not None:
            return db_quiz.user.token == self.user_token

        if db_quiz.user is not None:
            # Logged out user cannot own logged-in user's quiz
            return False

        return db_quiz.session_token == self.session_token
