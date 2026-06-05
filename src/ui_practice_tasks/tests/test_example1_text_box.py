"""
Task 01 — Text Box
URL: https://demoqa.com/text-box
"""

from playwright.sync_api import sync_playwright


URL = "https://demoqa.com/text-box"


def test_text_box_submission_displays_submitted_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        full_name = "John Carton"
        email = "john.carton@example.com"
        current_address = "123 Main St"
        permanent_address = "456 Other St"

        # ===== Arrange =====
        page.goto(URL)

        # ===== Act =====
        # Приклад заповнення одного поля:
        page.locator("#userName").fill(full_name)
        page.locator("#userEmail").fill(email)
        page.locator("#currentAddress").fill(current_address)
        page.locator("#permanentAddress").fill(permanent_address)


        # TODO: заповнити поле #userEmail значенням email
        # TODO: заповнити поле #currentAddress значенням current_address
        # TODO: заповнити поле #permanentAddress значенням permanent_address

        # TODO: клікнути по кнопці #submit
        # Підказка: якщо банер перекриває кнопку — page.locator("#submit").scroll_into_view_if_needed()
        page.locator("#submit").scroll_into_view_if_needed()
        page.wait_for_selector("#submit", state="visible")
        page.locator("#submit").click()

        # ===== Assert =====
        # Дочекатися появи блоку результату:
        page.locator("#output").wait_for(state="visible")

        # Приклад однієї перевірки:
        assert page.locator("#output").is_visible()

        # TODO: assert що full_name є у тексті локатора "#output #name"
        # Підказка: assert full_name in page.locator("#output #name").text_content()
        assert full_name in page.locator("#output #name").text_content()

        # TODO: assert що email є у тексті локатора "#output #email"
        # TODO: assert що current_address є у тексті локатора "#output #currentAddress"
        # TODO: assert що permanent_address є у тексті локатора "#output #permanentAddress"
        assert email in page.locator("#output #email").text_content()
        assert current_address in page.locator("#output #currentAddress").text_content()
        assert permanent_address in page.locator("#output #permanentAddress").text_content()

        browser.close()