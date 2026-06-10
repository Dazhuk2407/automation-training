from playwright.sync_api import Page


class RadioButtonPages:
    def __init__(self, page: Page):
        self._page = page

        self.locator_text_success = page.locator(".text-success")
        self.locator_yes_radio = page.locator("#yesRadio")
        self.locator_no_radio = page.locator("#noRadio")


    def click_by_yes_radio(self):
         self._page.get_by_text("Yes", exact=True).click()
         self.locator_text_success.wait_for(state="visible")

    def is_yes_radio_checked(self):
        return self.locator_yes_radio.is_checked()  
    
    def is_no_radio_disabled(self):
        return self.locator_no_radio.is_disabled()  
    
    def has_text_success_yes(self):
        return "Yes" in self.locator_text_success.text_content()
    
    

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

