from typing import Optional

from pydantic import BaseModel


class SessionData(BaseModel):
    created_at: str
    user_token: Optional[str]
