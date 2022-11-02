from pydantic import BaseModel

from models.user_role import UserRole


class User(BaseModel):
    """Representation of the DB object, whatever the Frontend might need to know about it"""
    token: str
    email_address: str
    role: UserRole = UserRole.ADMIN
