from __future__ import annotations

from typing import List, Union

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.connection import DbBase, Session
from database.db_types.string_enum_db_type import StringEnumDbType
from database.db_types.token_db_type import TokenDbType
from models.token import Token
from models.user import User
from models.user_role import UserRole


class DbUser(DbBase):
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True)
    token: Token = Column(TokenDbType, unique=True)
    email_address: str = Column(String, nullable=False)
    role: UserRole = Column(StringEnumDbType(UserRole), nullable=False)

    quizzes = relationship('DbQuiz', back_populates='user', lazy='select')

    def to_model(self) -> User:
        return User(
            token=self.token.value,
            email_address=self.email_address,
            role=self.role
        )

    @staticmethod
    def create_user(session: Session, email_address: str, role: UserRole) -> DbUser:
        db_user = DbUser(token=Token.generate_user_token(), email_address=email_address, role=role)
        session.add(db_user)
        return db_user

    @staticmethod
    def find_all_by_email_address(session: Session, email_address: str) -> List[DbUser]:
        return session.query(DbUser).filter(DbUser.email_address == email_address).all()

    @staticmethod
    def find_by_token(session: Session, token: Union[Token[User], str]) -> DbUser:
        token = token if isinstance(token, Token) else Token(value=token)
        return session.query(DbUser).filter(DbUser.token == token).one()
