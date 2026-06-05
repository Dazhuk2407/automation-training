"""
Task 05 — Web Tables
URL: https://demoqa.com/webtables
"""

from ui_practice_tasks.page_objects.home_page import HomePage
from ui_practice_tasks.page_objects.home_page import PageElements
from ui_practice_tasks.page_objects.child_pages import WebTablesPages
#from ui_practice_tasks.tests.conftest import go_to_web_tables



URL = "https://demoqa.com/webtables"


def test_web_tables_add_new_user_row_appears(web_tables_page):


          
        first_name1 = "Alice"
        last_name = "Cooper"
        email = "alice.cooper@example.com"
        age = "28"
        salary = "45000"
        department = "QA"

        # ===== Arrange =====
        #page.goto(URL)
        
        
        # ===== Act =====
        # Відкрити модалку додавання запису:
    

        
        web_tables_page.click_add_registration_form_button()
        web_tables_page.fill_reg_form(first_name=first_name1, last_name=last_name, email=email, age=age, salary=salary, department=department)
        web_tables_page.click_submit_button()


        # TODO: assert що модалка #registration-form-modal прихована
        # Підказка: метод .is_hidden()
        assert web_tables_page.locator_registration_form_modal.is_hidden()
        
        #page.pause()
        # TODO: assert що у таблиці .rt-tbody є email
        # Підказка: assert email in page.locator(".rt-tbody").text_content()
        assert page.locator("td", has_text=email).last.is_visible()

        # TODO: assert що у таблиці .rt-tbody є first_name
        assert page.locator("td", has_text=first_name1).first.is_visible()