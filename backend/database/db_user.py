from __future__ import annotations

from typing import List, Union

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.common import DbBase, Session
from database.token_db_type import TokenDbType
from models.token import Token
from quizzes.models import UserRole, User


class DbUser(DbBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    token = Column(TokenDbType, unique=True)
    email_address = Column(String, nullable=False)
    role = Column(String(50), nullable=False)

    quizzes = relationship('DbQuiz', back_populates='user', lazy='select')

    def to_model(self) -> User:
        return User(
            token=self.token.value,
            email_address=self.email_address,
            role=UserRole(self.role)
        )

    @staticmethod
    def create_user(session: Session, email_address: str, role: UserRole) -> DbUser:
        db_user = DbUser(token=Token.generate_user_token(), email_address=email_address, role=role.value)
        session.add(db_user)
        return db_user

    @staticmethod
    def find_all_by_email_address(session: Session, email_address: str) -> List[DbUser]:
        return session.query(DbUser).filter(DbUser.email_address == email_address).all()

    @staticmethod
    def find_by_token(session: Session, token: Union[Token[User], str]) -> DbUser:
        # token = token.value if isinstance(token, Token) else token
        token = token if isinstance(token, Token) else Token(value=token)
        return session.query(DbUser).filter(DbUser.token == token).one()
