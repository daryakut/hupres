from __future__ import annotations

from typing import List, Union

from sqlalchemy import Column, Integer, String

from database.common import DbBase, Session
from models.token import Token
from quiz_algorithm.models import UserRole, User


class DbUser(DbBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    token = Column(String(32), unique=True)
    email_address = Column(String, nullable=False)
    role = Column(String(50), nullable=False)

    def to_model(self) -> User:
        return User(
            token=self.token,
            email_address=self.email_address,
            role=UserRole(self.role)
        )

    @staticmethod
    def create_user(session: Session, email_address: str, role: UserRole) -> DbUser:
        db_user = DbUser(token=Token.generate_user_token().value, email_address=email_address, role=role.value)
        session.add(db_user)
        return db_user

    @staticmethod
    def find_all_by_email_address(session: Session, email_address: str) -> List[DbUser]:
        return session.query(DbUser).filter(DbUser.email_address == email_address).all()

    @staticmethod
    def find_by_token(session: Session, token: Union[Token[User], str]) -> DbUser:
        token = token.value if isinstance(token, Token) else token
        return session.query(DbUser).filter(DbUser.token == token).one()
