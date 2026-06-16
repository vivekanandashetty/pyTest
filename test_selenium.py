import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver(request):

    driver = webdriver.Chrome()

    request.cls.driver = driver

    yield

    driver.quit()


@pytest.mark.usefixtures("driver")
class TestGoogle:

    def test_title(self):
        self.driver.get("https://google.com")
        assert "Google" in self.driver.title

    def test_url(self):
        inputValue = "google"
        #inputValue = input("Enter the value to search: ")
        assert inputValue in self.driver.current_url.lower()