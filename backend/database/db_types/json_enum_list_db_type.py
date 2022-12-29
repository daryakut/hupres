import json
from enum import Enum
from typing import Optional, List

from sqlalchemy.types import TypeDecorator, String


class JsonEnumListDbType(TypeDecorator):
    impl = String(100)
    cache_ok = True

    def __init__(self, enum_type, *args, **kwargs):
        super(JsonEnumListDbType, self).__init__(*args, **kwargs)
        assert issubclass(enum_type, Enum), "enum_type must be a subclass of enum.Enum"
        self.enum_type = enum_type

    def process_bind_param(self, value: Optional[List[Enum]], dialect) -> Optional[str]:
        if value is None:
            return None
        return json.dumps([v.value for v in value])

    def process_result_value(self, value: Optional[str], dialect) -> Optional[List[Enum]]:
        if value is None:
            return None
        if isinstance(value, list):
            return [self.enum_type(v) for v in value]
        json_value = json.loads(value)
        return [self.enum_type(v) for v in json_value]
