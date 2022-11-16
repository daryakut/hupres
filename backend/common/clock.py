from datetime import datetime

from common.env import env
from tests.common.fake_clock import get_fake_clock


class Clock:

    def now(self) -> datetime:
        return datetime.utcnow()

    def now_ms(self) -> int:
        return int(self.now().timestamp() * 1000)


clock = Clock() if env.is_not_test() else get_fake_clock()
