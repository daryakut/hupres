from enum import Enum
from typing import Optional

from sqlalchemy.types import TypeDecorator, Integer


class IntEnumDbType(TypeDecorator):
    impl = Integer
    cache_ok = True

    def __init__(self, enum_type, *args, **kwargs):
        super(IntEnumDbType, self).__init__(*args, **kwargs)
        assert issubclass(enum_type, Enum), "enum_type must be a subclass of enum.Enum"
        self.enum_type = enum_type

    def process_bind_param(self, value: Optional[Enum], dialect) -> Optional[str]:
        if value is None:
            return None
        return value.value

    def process_result_value(self, value: Optional[str], dialect) -> Optional[Enum]:
        if value is None:
            return None
        return self.enum_type(value)
