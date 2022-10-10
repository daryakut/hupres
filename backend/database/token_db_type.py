from sqlalchemy.types import TypeDecorator, String

from models.token import Token


class TokenDbType(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        print("Converting Token object to string:", value)
        if value is None:
            return None
        if hasattr(value, 'value'):
            return value.value
        return value

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return Token(value=value)
