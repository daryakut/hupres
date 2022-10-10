from sqlalchemy.types import TypeDecorator, String

from models.token import Token


class TokenDbType(TypeDecorator):
    impl = String(64)

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return Token(value=value)
