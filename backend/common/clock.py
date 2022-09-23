from datetime import datetime


def now() -> datetime:
    return datetime.now()


def now_ms() -> int:
    return int(datetime.now().timestamp() * 1000)
