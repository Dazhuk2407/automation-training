"""
Task 06 — Practice Form
URL: https://demoqa.com/automation-practice-form
"""

from playwright.sync_api import sync_playwright


URL = "https://demoqa.com/automation-practice-form"


def test_practice_form_submission_shows_modal_with_correct_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        first_name = "John"
        last_name = "Carton"
        email = "john.carton@example.com"
        mobile = "1234567890"
        address = "123 Main St"

        # ===== Arrange =====
        page.goto(URL)

        # ===== Act =====
        # Приклад заповнення одного поля:
        page.locator("#firstName").fill(first_name)

        # TODO: заповнити #lastName значенням last_name
        # TODO: заповнити #userEmail значенням email

        # Обрати стать (радіо приховано за label, тому клікаємо по тексту):
        page.get_by_text("Male", exact=True).click()

        # TODO: заповнити #userNumber значенням mobile
        # TODO: заповнити #currentAddress значенням address

        # Прокрутити до Submit та клікнути.
        # force=True потрібен, бо банер реклами може перекривати кнопку:
        page.locator("#submit").scroll_into_view_if_needed()
        page.locator("#submit").click(force=True)

        # ===== Assert =====
        # Дочекатися появи модалки:
        page.locator(".modal-content").wait_for(state="visible")

        # TODO: assert що .modal-content видима
        # Підказка: метод .is_visible()

        # TODO: assert що заголовок #example-modal-sizes-title-lg
        #       дорівнює "Thanks for submitting the form"
        # Підказка: .text_content() == "..."

        # TODO: assert що у .modal-body є рядок "John Carton"
        # Підказка: assert f"{first_name} {last_name}" in page.locator(".modal-body").text_content()

        # TODO: assert що у .modal-body є email
        # TODO: assert що у .modal-body є mobile

        browser.close()