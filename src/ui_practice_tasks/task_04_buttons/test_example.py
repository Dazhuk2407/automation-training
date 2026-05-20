"""
Task 04 — Buttons
URL: https://demoqa.com/buttons
"""

from playwright.sync_api import sync_playwright


URL = "https://demoqa.com/buttons"


def test_buttons_double_right_and_single_click_messages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ===== Arrange =====
        page.goto(URL)

        # ===== Act =====
        # Приклад подвійного кліку:
        page.locator("#doubleClickBtn").dblclick()

        # TODO: правий клік по #rightClickBtn
        # Підказка: page.locator("#rightClickBtn").click(button="right")

        # TODO: звичайний клік по кнопці "Click Me"
        # Підказка: page.get_by_role("button", name="Click Me", exact=True).click()

        # ===== Assert =====
        # Дочекатися появи повідомлень:
        page.locator("#doubleClickMessage").wait_for(state="visible")
        page.locator("#rightClickMessage").wait_for(state="visible")
        page.locator("#dynamicClickMessage").wait_for(state="visible")

        # TODO: assert що #doubleClickMessage має текст "You have done a double click"
        # Підказка: assert page.locator("#doubleClickMessage").text_content() == "You have done a double click"

        # TODO: assert що #rightClickMessage має текст "You have done a right click"
        # TODO: assert що #dynamicClickMessage має текст "You have done a dynamic click"

        browser.close()