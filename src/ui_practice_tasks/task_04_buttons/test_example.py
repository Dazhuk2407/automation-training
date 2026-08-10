"""
Task 04 — Buttons
URL: https://demoqa.com/buttons
"""

from playwright.sync_api import sync_playwright
from ui_practice_tasks.POM_Pattern import LocatorsTask4
from ui_practice_tasks.POM_Pattern import CommonActions




URL = "https://demoqa.com/buttons"


def test_buttons_double_right_and_single_click_messages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        locators_task4 = LocatorsTask4(page)
        common_actions = CommonActions(page)

        # ===== Arrange =====
        common_actions.open_url(URL)
        #page.goto(URL)
        page.pause()
        # ===== Act =====
        # Приклад подвійного кліку:
        #page.locator("#doubleClickBtn").dblclick()
        common_actions.action_double_click(locators_task4.locator_double_click_btn, "You have done a double click")

        # TODO: правий клік по #rightClickBtn
        common_actions.action_right_click(locators_task4.locator_right_click_btn, "You have done a right click")
        # Підказка: page.locator("#rightClickBtn").click(button="right")

        # TODO: звичайний клік по кнопці "Click Me"
        # Підказка: page.get_by_role("button", name="Click Me", exact=True).click()
        common_actions.action_click_by_text("Click Me")
       
       
        # ===== Assert =====
        # Дочекатися появи повідомлень:
        # page.locator("#doubleClickMessage").wait_for(state="visible")
        # page.locator("#rightClickMessage").wait_for(state="visible")
        # page.locator("#dynamicClickMessage").wait_for(state="visible")

        common_actions.locator_wait_for_state(locators_task4.locator_double_click_message)
        common_actions.locator_wait_for_state(locators_task4.locator_right_click_message)
        common_actions.locator_wait_for_state(locators_task4.locator_dynamic_click_message)

        # TODO: assert що #doubleClickMessage має текст "You have done a double click"
        # Підказка: assert page.locator("#doubleClickMessage").text_content() == "You have done a double click"
        assert common_actions.text_verification(locators_task4.locator_double_click_message, "You have done a double click")
        
        # TODO: assert що #rightClickMessage має текст "You have done a right click"
        assert common_actions.text_verification(locators_task4.locator_right_click_message, "You have done a right click")
        
        # TODO: assert що #dynamicClickMessage має текст "You have done a dynamic click"
        assert common_actions.text_verification(locators_task4.locator_dynamic_click_message, "You have done a dynamic click")

        browser.close()