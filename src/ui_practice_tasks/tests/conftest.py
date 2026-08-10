import pytest
from playwright.sync_api import sync_playwright

from ui_practice_tasks.pages.home_page import HomePage


BASE_URL = "https://demoqa.com"


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
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

@pytest.fixture
def buttons_page(home_page):
    return home_page.open_buttons_page()

@pytest.fixture
def check_box_page(home_page):
    return home_page.open_check_box_page()

@pytest.fixture
def practice_form_page(home_page):
    return home_page.open_practice_form_page()

@pytest.fixture
def radio_button_page(home_page):
    return home_page.open_radio_button_page()

@pytest.fixture
def text_box_page(home_page):
    return home_page.open_text_box_page()



