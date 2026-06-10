from playwright.sync_api import Page


class ButtonsPages:
    def __init__(self, page: Page):
        self._page = page
        self.locator_double_click_btn = page.locator("#doubleClickBtn")
        self.locator_right_click_btn = page.locator("#rightClickBtn")
        self.locator_dynamic_click_btn = page.locator("button:has-text('Click Me')")
        self.locator_double_click_message = page.locator("#doubleClickMessage")
        self.locator_right_click_message = page.locator("#rightClickMessage")
        self.locator_dynamic_click_message = page.locator("#dynamicClickMessage")

    def click_by_double_click_btn(self):
        self.locator_double_click_btn.dblclick()
        self.locator_double_click_message.wait_for(state="visible")

    def click_by_right_click_btn(self):
        self.locator_right_click_btn.click(button="right")
        self.locator_right_click_message.wait_for(state="visible")

    def click_by_dynamic_click_btn(self):
        self.locator_dynamic_click_btn.last.click()
        self.locator_dynamic_click_message.wait_for(state="visible")


    def has_double_click_message(self):
        return "You have done a double click" in self.locator_double_click_message.text_content()
    
    def has_right_click_message(self):
        return "You have done a right click" in self.locator_right_click_message.text_content() 
    
    def has_dynamic_click_message(self):
        return "You have done a dynamic click" in self.locator_dynamic_click_message.text_content()