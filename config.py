import os

BASE_URLS = {
    "QA": "https://qa.example.com",
    "UAT": "https://uat.example.com",
    "PROD": "https://example.com"
}


ENV = os.getenv("ENV", "QA")
BASE_URL = BASE_URLS[ENV]