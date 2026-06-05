
from playwright.async_api import expect
from playwright.sync_api import sync_playwright
import pytest

from ui_practice_tasks.page_objects.home_page import HomePage, PageElements
from ui_practice_tasks.page_objects.child_pages import WebTablesPages

BASE_URL = "https://demoqa.com"

@pytest.fixture
def web_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture()
def go_home(page):
    page.goto(BASE_URL)
    return HomePage(page)
    #expect(page).to_have_url(BASE_URL)



@pytest.fixture()
def web_tables_page(go_home):
    home_page = HomePage(go_home)
    home_page.click_on_elements_link()
    home_page.extend_list(PageElements.LINK_ELEMENTS.value)
    home_page.click_on_elements_list(PageElements.LIST_WEB_TABLES.value)
    return WebTablesPages(go_home.page)