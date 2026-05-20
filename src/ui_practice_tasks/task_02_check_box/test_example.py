"""
Task 02 — Check Box
URL: https://demoqa.com/checkbox
"""

from playwright.sync_api import sync_playwright


URL = "https://demoqa.com/checkbox"


def test_checkbox_selection_shows_result():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ===== Arrange =====
        page.goto(URL)

        # ===== Act =====
        # Розгорнути все дерево одним кліком:
        page.locator('button[title="Expand all"]').click()

        # TODO: клікнути по чекбоксу ноди Desktop
        # Підказка: page.locator('label[for="tree-node-desktop"] .rct-checkbox').click()

        # ===== Assert =====
        # Дочекатися появи блоку результату:
        page.locator("#result").wait_for(state="visible")

        # TODO: assert що блок #result видимий
        # Підказка: assert page.locator("#result").is_visible()

        # TODO: assert що рядок "desktop" є у тексті #result
        # Підказка: assert "desktop" in page.locator("#result").text_content()

        # TODO: assert що інпут #tree-node-desktop у стані checked
        # Підказка: метод .is_checked()

        browser.close()