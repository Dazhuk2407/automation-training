"""
Task 03 — Radio Button
URL: https://demoqa.com/radio-button
"""

from playwright.sync_api import sync_playwright


URL = "https://demoqa.com/radio-button"


def test_radio_button_selects_yes_and_no_is_disabled():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ===== Arrange =====
        page.goto(URL)

        # ===== Act =====
        # Інпут радіо прихований за label, тому клікаємо по тексту:
        page.get_by_text("Yes", exact=True).click()

        # ===== Assert =====
        # Дочекатися появи тексту результату:
        page.locator(".text-success").wait_for(state="visible")

        # TODO: assert що інпут #yesRadio у стані checked
        # Підказка: метод .is_checked()

        # TODO: assert що у локаторі .text-success є слово "Yes"
        # Підказка: assert "Yes" in page.locator(".text-success").text_content()

        # TODO: assert що інпут #noRadio у стані disabled
        # Підказка: метод .is_disabled()

        browser.close()