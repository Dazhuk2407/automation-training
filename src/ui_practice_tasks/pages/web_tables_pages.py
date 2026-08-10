from playwright.sync_api import Page


class WebTablesPages:
    def __init__(self, page: Page):
        self._page = page

        self.locator_add_new_record_button = page.locator("#addNewRecordButton")
        self.locator_first_name_input = page.locator("#firstName")
        self.locator_last_name_input = page.locator("#lastName")
        self.locator_email_input = page.locator("#userEmail")
        self.locator_age_input = page.locator("#age")
        self.locator_salary_input = page.locator("#salary")
        self.locator_department_input = page.locator("#department")
        self.locator_submit_button = page.locator("#submit")
        self.locator_registration_form_modal = page.locator("#registration-form-modal")

    def click_add_registration_form_button(self):
        self.locator_add_new_record_button.click()

    def fill_reg_form(self, first_name, last_name, email, age, salary, department):
        self.locator_first_name_input.fill(first_name)
        self.locator_last_name_input.fill(last_name)
        self.locator_email_input.fill(email)
        self.locator_age_input.fill(age)
        self.locator_salary_input.fill(salary)
        self.locator_department_input.fill(department)

    def click_submit_button(self):
        self.locator_submit_button.click()
        self.locator_registration_form_modal.wait_for(state="hidden")

    def is_registration_form_hidden(self):
        return self.locator_registration_form_modal.is_hidden()

    def has_email_in_table(self, email):
        return self._page.locator("td", has_text=email).last.is_visible()

    def has_first_name_in_table(self, first_name):
        return self._page.locator("td", has_text=first_name).first.is_visible()
