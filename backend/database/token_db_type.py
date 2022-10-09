from sqlalchemy.types import TypeDecorator, String

from models.token import Token


class TokenDbType(TypeDecorator):
    impl = String

    def process_bind_param(self, value: Token, dialect):
        # Convert Token object to string when writing to DB
        return value.value

    def process_result_value(self, value: str, dialect):
        # Convert string back to Token object when reading from DB
        return Token(value)
