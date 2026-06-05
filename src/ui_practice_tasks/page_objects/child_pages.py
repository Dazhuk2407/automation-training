from playwright.sync_api import Page
from playwright.sync_api import sync_playwright



class LocatorsTask3:
    def __init__(self, page: Page):
        self.page = page        
        self.locator_text_success = page.locator(".text-success")
        self.locator_yes_radio = page.locator("#yesRadio")
        self.locator_no_radio = page.locator("#noRadio")
    
class LocatorsTask4:
    def __init__(self, page: Page):
        self.page = page        
        self.locator_double_click_btn = page.locator("#doubleClickBtn")
        self.locator_right_click_btn = page.locator("#rightClickBtn")
        self.locator_dynamic_click_btn = page.locator("button:has-text('Click Me')")
        self.locator_double_click_message = page.locator("#doubleClickMessage")
        self.locator_right_click_message = page.locator("#rightClickMessage")
        self.locator_dynamic_click_message = page.locator("#dynamicClickMessage")

class WebTablesPages:
    def __init__(self, page: Page):
        self.page = page        
        self.locator_add_new_record_button = page.locator("#addNewRecordButton")
        self.locator_first_name_input = page.locator("#firstName")
        self.locator_last_name_input = page.locator("#lastName")
        self.locator_email_input = page.locator("#userEmail")
        self.locator_age_input = page.locator("#age")   
        self.locator_salary_input = page.locator("#salary")
        self.locator_department_input = page.locator("#department")
        self.locator_submit_button = page.locator("#submit")
        self.locator_registration_form_modal = page.locator("#registration-form-modal")
        self.locator_tr_tbody = page.locator("td")

    def click_add_registration_form_button(self):
        self.locator_add_new_record_button.click()  
        #TODO add POPup verification

    def fill_reg_form(self, first_name: str, last_name: str, email: str, age: str, salary: str, department):
 
        # Приклад заповнення одного поля у модалці:
        self.locator_first_name_input.fill(first_name)

        # TODO: заповнити #lastName значенням last_name
        self.locator_last_name_input.fill(last_name)
        # TODO: заповнити #userEmail значенням email
        self.locator_email_input.fill(email)
        # TODO: заповнити #age значенням age
        self.locator_age_input.fill(age)
        # TODO: заповнити #salary значенням salary
        self.locator_salary_input.fill(salary)
        # TODO: заповнити #department значенням department
        self.locator_department_input.fill(department)
        # TODO: клікнути по кнопці Submit у модалці
        # Підказка: page.locator("#submit").click()


    def click_submit_button(self):
        self.locator_submit_button.click()

        # ===== Assert =====
        # Дочекатися закриття модалки:
        self.locator_registration_form_modal.wait_for(state="hidden")


class CommonActions:
    def __init__(self, page: Page):
        self.page = page

        
    def open_url(self, url: str):
        self.page.goto(url)


    def action_click_by_text(self, text: str, exact: bool = True):
        self.page.get_by_text(text, exact=exact).click()


    def locator_wait_for_state(self, locator, state: str = "visible"):
         locator.wait_for(state=state)


    def input_verification_is_checked(self, locator):
        return locator.is_checked()
    
    def text_verification(self, locator, text: str):
        return text in locator.text_content()
    
    def action_double_click(self, locator):
        locator.dblclick()

    def action_right_click(self, locator):
        locator.click(button="right")

    def action_click(self, locator):
        locator.click()

    def action_fill(self, locator, value: str):
        locator.fill(value)