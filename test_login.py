import pytest

@pytest.fixture
def setup():
    print("Setup")
    yield
    print("Teardown")

class TestLogin:

    def test_valid_login(self, setup):
        print("Valid Login Test")

    def test_invalid_login(self, setup):
        print("Invalid Login Test")