import pytest

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    return request.param

def test_browser(browser):
    print(f"\nBrowser: {browser}")
    print(browser)
    