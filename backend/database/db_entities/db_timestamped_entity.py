from __future__ import annotations

from sqlalchemy import Column, DateTime

from database.connection import DbBase


class DbTimestampedEntity(DbBase):
    created_at = Column(DateTime)
    updated_at = Column(DateTime)