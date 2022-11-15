import time

import pytest

from common.time_limit import time_limit


def test_must_timeout_when_waiting_for_too_long():
    with pytest.raises(TimeoutError) as e:
        with time_limit(100):
            time.sleep(5)


def test_must_not_timeout_when_waiting_for_not_too_long():
    with time_limit(1000):
        time.sleep(0.1)
