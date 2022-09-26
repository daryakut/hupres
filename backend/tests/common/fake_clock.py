from datetime import datetime

_fake_instance = None


class FakeClock:
    current_time: datetime = datetime(2023, 9, 1, 00, 00, 00)

    def now(self) -> datetime:
        return self.current_time

    def now_ms(self) -> int:
        return int(self.current_time.timestamp() * 1000)


def get_fake_clock() -> FakeClock:
    # This way we emulate a singleton that is not created when module is imported unless this method is called
    global _fake_instance
    if _fake_instance is None:
        _fake_instance = FakeClock()

    return _fake_instance
