import threading
from contextlib import contextmanager


@contextmanager
def time_limit(milliseconds):
    def signal_handler():
        raise TimeoutError("Operation timed out")

    timer = threading.Timer(milliseconds * 1000, signal_handler)
    timer.start()
    try:
        yield
    finally:
        timer.cancel()
