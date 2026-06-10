from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

class PracticeFormPages:
    def __init__(self, page: Page):
        self._page = page

        self.locator_input_first_name = page.locator("#firstName")
        self.locator_input_last_name = page.locator("#lastName")
        self.locator_input_email = page.locator("#userEmail")
        self.locator_input_mobile = page.locator("#userNumber")
        self.locator_input_address = page.locator("#currentAddress")
        self.locator_submit_button = page.locator("#submit")
        self.locator_modal_content = page.locator(".modal-content")
        self.locator_modal_title = page.locator("#example-modal-sizes-title-lg")
        self.locator_modal_body = page.locator(".modal-body")



    def fill_form(self, first_name: str, last_name: str, email: str, mobile: str, address: str):
        self.locator_input_first_name.fill(first_name)
        self.locator_input_last_name.fill(last_name)
        self.locator_input_email.fill(email)
        self._page.get_by_text("Male", exact=True).click()
        self.locator_input_address.fill(address)
        self.locator_input_mobile.fill(mobile)


    def submit_form(self):
        self.locator_submit_button.scroll_into_view_if_needed()    
        self.locator_submit_button.click(force=True)

    def wait_for_modal(self):
        self.locator_modal_content.wait_for(state="visible")
        self.locator_modal_title.wait_for(state="visible")

    def has_title(self):
        return self.locator_modal_title.text_content() == "Thanks for submitting the form"
    
    def has_full_name_in_modal(self, first_name, last_name):
        return f"{first_name} {last_name}" in self.locator_modal_body.text_content()
    
    def has_email_in_modal(self, email):
        return f"{email}" in self.locator_modal_body.text_content() 
    
    def has_mobile_in_modal(self, mobile):
        return f"{mobile}" in self.locator_modal_body.text_content()    