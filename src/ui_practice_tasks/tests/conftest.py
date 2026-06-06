import pytest
from playwright.sync_api import sync_playwright

from ui_practice_tasks.pages.home_page import HomePage


BASE_URL = "https://demoqa.com"


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        yield page

        browser.close()


@pytest.fixture
def home_page(page):
    page.goto(BASE_URL)
    return HomePage(page)


@pytest.fixture
def web_tables_page(home_page):
    return home_page.open_web_tables_page()
