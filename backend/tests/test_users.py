class TestUsers:
    def setup_module(self, method):
        print(f"Setting up for {method.__name__}")

    def can_create_user(self):
        assert 3 + 3 == 6
