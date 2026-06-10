from playwright.sync_api import Page


class TextBoxPages:
    def __init__(self, page: Page):
        self._page = page

        self.locator_input_userName = page.locator("#userName")
        self.locator_input_userEmail = page.locator("#userEmail")
        self.locator_input_currentAddress = page.locator("#currentAddress")
        self.locator_input_permanentAddress = page.locator("#permanentAddress")
        self.locator_submit_button = page.locator("#submit")
        self.locator_output_block = page.locator("#output")
   

    def fill_text_box_form(self, full_name, email, current_address, permanent_address):
        self.locator_input_userName.fill(full_name)
        self.locator_input_userEmail.fill(email)
        self.locator_input_currentAddress.fill(current_address)
        self.locator_input_permanentAddress.fill(permanent_address)


    def submit_form(self):
        self.locator_submit_button.scroll_into_view_if_needed()
        self._page.wait_for_selector("#submit", state="visible")
        self.locator_submit_button.click()

    def is_output_block_visible(self):
        self.locator_output_block.wait_for(state="visible")
        assert self.locator_output_block.is_visible()

    def has_full_name_in_output(self, full_name):
        assert full_name in self.locator_output_block.locator("#name").text_content()

    def has_email_in_output(self, email):
        assert email in self.locator_output_block.locator("#email").text_content()

    def has_current_address_in_output(self, current_address):
        assert current_address in self.locator_output_block.locator("#currentAddress").text_content()

    def has_permanent_address_in_output(self, permanent_address):
        assert permanent_address in self.locator_output_block.locator("#permanentAddress").text_content()