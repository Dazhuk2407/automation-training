"""
Task 03 — Radio Button
URL: https://demoqa.com/radio-button
"""

from playwright.sync_api import sync_playwright
from ui_practice_tasks.POM_Pattern import LocatorsTask3
from ui_practice_tasks.POM_Pattern import CommonActions



URL = "https://demoqa.com/radio-button"


def test_radio_button_selects_yes_and_no_is_disabled():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        locators_task3 = LocatorsTask3(page)
        common_actions = CommonActions(page)
        
        # ===== Arrange =====
        common_actions.open_url(URL)
        #page.goto(URL)

        # ===== Act =====
        # Інпут радіо прихований за label, тому клікаємо по тексту:
        #page.get_by_text("Yes", exact=True).click()
        common_actions.action_click_by_text("Yes")

        # ===== Assert =====
        # Дочекатися появи тексту результату:
        #page.locator(".text-success").wait_for(state="visible")
        common_actions.locator_wait_for_state(locators_task3.locator_text_success)
       
        
        # TODO: assert що інпут #yesRadio у стані checked
        # Підказка: метод .is_checked()
        assert common_actions.input_verification_is_checked(locators_task3.locator_yes_radio)

        # TODO: assert що у локаторі .text-success є слово "Yes"
        # Підказка: assert "Yes" in page.locator(".text-success").text_content()
        assert common_actions.text_verification(locators_task3.locator_text_success, "Yes")

        # TODO: assert що інпут #noRadio у стані disabled
        # Підказка: метод .is_disabled()
        assert common_actions.input_verification_is_checked(locators_task3.locator_no_radio) == False

        browser.close()