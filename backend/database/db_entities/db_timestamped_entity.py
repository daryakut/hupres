from __future__ import annotations

from sqlalchemy import Column, DateTime

from common.clock import clock


class DbTimestampedEntity:
    created_at = Column(DateTime, default=clock.now)
    updated_at = Column(DateTime, default=clock.now, onupdate=clock.now)
