"""
Pytest should only run classes that end with `Test` and methods that start with `test_`. We don't want to run
classes with prefix Test because they can be TestUtils or TestService classes
"""


class ThisMustRunTest:
    """Only classes that end with "Test" will be run by pytest."""

    def test_must_run(self):
        assert 2 + 2 == 4

    def must_not_run_test(self):
        """Only methods that start with "test_" will be run by pytest."""
        assert 2 + 2 == 5


class TestThisMustNotRun:
    """Classes that start with "Test" should not run so that we can build various TestUtils."""

    def test_must_not_run(self):
        assert 2 + 2 == 6


def test_must_run():
    assert 2 + 2 == 4


def must_not_run_test():
    """Only methods that start with "test_" will be run by pytest."""
    assert 2 + 2 == 5
