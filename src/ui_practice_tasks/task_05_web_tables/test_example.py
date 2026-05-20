"""
Task 05 — Web Tables
URL: https://demoqa.com/webtables
"""

from playwright.sync_api import sync_playwright


URL = "https://demoqa.com/webtables"


def test_web_tables_add_new_user_row_appears():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        first_name = "Alice"
        last_name = "Cooper"
        email = "alice.cooper@example.com"
        age = "28"
        salary = "45000"
        department = "QA"

        # ===== Arrange =====
        page.goto(URL)

        # ===== Act =====
        # Відкрити модалку додавання запису:
        page.locator("#addNewRecordButton").click()

        # Приклад заповнення одного поля у модалці:
        page.locator("#firstName").fill(first_name)

        # TODO: заповнити #lastName значенням last_name
        # TODO: заповнити #userEmail значенням email
        # TODO: заповнити #age значенням age
        # TODO: заповнити #salary значенням salary
        # TODO: заповнити #department значенням department

        # TODO: клікнути по кнопці Submit у модалці
        # Підказка: page.locator("#submit").click()

        # ===== Assert =====
        # Дочекатися закриття модалки:
        page.locator("#registration-form-modal").wait_for(state="hidden")

        # TODO: assert що модалка #registration-form-modal прихована
        # Підказка: метод .is_hidden()

        # TODO: assert що у таблиці .rt-tbody є email
        # Підказка: assert email in page.locator(".rt-tbody").text_content()

        # TODO: assert що у таблиці .rt-tbody є first_name

        browser.close()