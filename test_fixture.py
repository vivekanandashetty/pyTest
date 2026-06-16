import pytest

@pytest.fixture
def setup():
    print("Setup")
    yield
    print("Teardown")

def test_login(setup):
    print("Executing Login Test")
    assert True