from typing import Optional

from sqlalchemy.types import TypeDecorator, String

from models.token import Token


class TokenDbType(TypeDecorator):
    impl = String(64)

    def process_bind_param(self, value: Optional[Token], dialect) -> Optional[str]:
        if value is None:
            return None
        return value.value

    def process_result_value(self, value: Optional[str], dialect) -> Optional[Token]:
        if value is None:
            return None
        return Token(value=value)
