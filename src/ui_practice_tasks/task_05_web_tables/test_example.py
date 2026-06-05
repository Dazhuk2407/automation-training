"""
Task 05 — Web Tables
URL: https://demoqa.com/webtables
"""

from playwright.sync_api import sync_playwright
from ui_practice_tasks.POM_Pattern import WebTablesPages
from ui_practice_tasks.POM_Pattern import CommonActions
from ui_practice_tasks.POM_Pattern import HomePage
from ui_practice_tasks.task_05_web_tables.page_objects import home_page


URL = "https://demoqa.com/webtables"


def test_web_tables_add_new_user_row_appears():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        locators_task5 = WebTablesPages(page)
        common_actions = CommonActions(page)
        

        first_name = "Alice"
        last_name = "Cooper"
        email = "alice.cooper@example.com"
        age = "28"
        salary = "45000"
        department = "QA"

        # ===== Arrange =====
        #page.goto(URL)
        common_actions.open_url(URL)
        home_page = HomePage(page)
        home_page.click_elements_card()

        web_tables_page = WebTablesPages(page)
        


        # ===== Act =====
        # Відкрити модалку додавання запису:
        #page.locator("#addNewRecordButton").click()
        common_actions.action_click(locators_task5.locator_add_new_record_button)

        # Приклад заповнення одного поля у модалці:
        #page.locator("#firstName").fill(first_name)
        common_actions.action_fill(locators_task5.locator_first_name_input, first_name)

        # TODO: заповнити #lastName значенням last_name
        common_actions.action_fill(locators_task5.locator_last_name_input, last_name)
        # TODO: заповнити #userEmail значенням email
        common_actions.action_fill(locators_task5.locator_email_input, email)
        # TODO: заповнити #age значенням age
        common_actions.action_fill(locators_task5.locator_age_input, age)
        # TODO: заповнити #salary значенням salary
        common_actions.action_fill(locators_task5.locator_salary_input, salary)
        # TODO: заповнити #department значенням department
        common_actions.action_fill(locators_task5.locator_department_input, department)
        page.pause()
        # TODO: клікнути по кнопці Submit у модалці
        # Підказка: page.locator("#submit").click()
        common_actions.action_click(locators_task5.locator_submit_button)

        # ===== Assert =====
        # Дочекатися закриття модалки:
        #page.locator("#registration-form-modal").wait_for(state="hidden")
        common_actions.locator_wait_for_state(locators_task5.locator_registration_form_modal, state="hidden")

        # TODO: assert що модалка #registration-form-modal прихована
        # Підказка: метод .is_hidden()
        assert locators_task5.locator_registration_form_modal.is_hidden()
        
        #page.pause()
        # TODO: assert що у таблиці .rt-tbody є email
        # Підказка: assert email in page.locator(".rt-tbody").text_content()
        assert page.locator("td", has_text=email).last.is_visible()

        # TODO: assert що у таблиці .rt-tbody є first_name
        #assert common_actions.text_verification(locators_task5.locator_tr_tbody, first_name)
        assert page.locator("td", has_text=first_name).first.is_visible()


        browser.close()