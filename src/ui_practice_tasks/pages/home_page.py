from playwright.sync_api import Page
from enum import Enum
from ui_practice_tasks.pages.web_tables_pages import WebTablesPages
from ui_practice_tasks.pages.buttons_pages import ButtonsPages
from ui_practice_tasks.pages.check_box_pages import CheckBoxPages
from ui_practice_tasks.pages.practice_form_pages import PracticeFormPages
from ui_practice_tasks.pages.radio_button_pages import RadioButtonPages
from ui_practice_tasks.pages.text_box_pages import TextBoxPages



class PageElements(Enum):
    LINK_ELEMENTS= "elements"
    LINK_FORMS  = "forms"
    LINK_WIDGETS = "widgets"
    LIST_TEXT_BOX_ = "Text Box"
    LIST_WEB_TABLES = "Web Tables"
    LIST_RADIO_BUTTONS = "Radio Button"
    LIST_CHECK_BOXES = "Check Box"
    LIST_BUTTONS = "Buttons"
    LIST_PRACTICE_FORM = "Practice Form"


class HomePage:
    def __init__(self, page: Page):
        self._page = page

        self.elements_card = page.locator("h5",
                                          has_text=PageElements.LINK_ELEMENTS.value)
        self.forms_card = page.locator("h5",
                                          has_text=PageElements.LINK_FORMS.value)
        self.text_box_item = page.locator("span",
                                            has_text=PageElements.LIST_TEXT_BOX_.value)
        self.radio_button_item = page.locator("span",
                                            has_text=PageElements.LIST_RADIO_BUTTONS.value)
        self.web_tables_item = page.locator("span",
                                            has_text=PageElements.LIST_WEB_TABLES.value)
        self.check_box_item = page.locator("span",
                                            has_text=PageElements.LIST_CHECK_BOXES.value)
        self.buttons_item = page.locator("span",
                                            has_text=PageElements.LIST_BUTTONS.value)
        self.practice_form_item = page.locator("span",
                                                has_text=PageElements.LIST_PRACTICE_FORM.value)

    def open_web_tables_page(self):
        self.elements_card.click()
        self.web_tables_item.click()
        self._page.wait_for_url("**/webtables")
        return WebTablesPages(self._page)
    
    def open_text_box_page(self):
        self.elements_card.click()
        self.text_box_item.click(position={"x": 2, "y": 5})
        self._page.wait_for_url("**/text-box")
        return TextBoxPages(self._page)
    
    def open_radio_button_page(self):
        self.elements_card.click()
        self.radio_button_item.click(position={"x": 2, "y": 5})
        self._page.wait_for_url("**/radio-button")
        return RadioButtonPages (self._page)
    
    def open_check_box_page(self):
        self.elements_card.click()
        self.check_box_item.click(position={"x": 2, "y": 5})
        self._page.wait_for_url("**/checkbox")
        return CheckBoxPages (self._page)
    
    def open_buttons_page(self):
        self.elements_card.click()
        self.buttons_item.click()
        self._page.wait_for_url("**/buttons")
        return ButtonsPages (self._page)

    def open_practice_form_page(self):
        self.forms_card.click()
        self.practice_form_item.click()
        self._page.wait_for_url("**/automation-practice-form")
        return PracticeFormPages (self._page)