from unicodedata import name

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from enum import Enum


class PageElements(Enum):
    LINK_ELEMENTS= "elements"
    LINK_FORMS  = "forms"
    LINK_WIDGETS = "widgets"
    LIST_TEXT_BOX_ = "Text Box"
    LIST_WEB_TABLES = "Web Tables"

class HomePage:

    def __init__(self, page: Page):
        self.page = page   
        self.locator_element_list = page.locator(".element-list.accordion-collapse.collapse.show")   
        self.locator_list_text_box = page.locator("#item-0")  
        self.locator_list_check_box = page.locator("#item-1")  
        self.locator_list_radio_button = page.locator("#item-2")  
        self.locator_list_web_tables = page.locator("#item-3") 
        self.locator_list_buttons = page.locator("#item-4")
        self.locator_list_links = page.locator("#item-5")



    def click_on_elements_link(self, child_element: str = PageElements.LINK_ELEMENTS.value):     
        self.page.get_by_role('link', name=child_element).click()
        self.page.wait_for_load_state("load")

    def click_on_elements_list(self, child_element: str = PageElements.LIST_WEB_TABLES.value):     
        self.page.get_by_text(child_element, exact=True).click()
        self.page.wait_for_load_state("load")

    def extend_list(self, extended_element):
        if not self.locator_element_list.is_visible():
            self.page.get_by_role('link', name=extended_element).click()
            self.page.wait_for_load_state("load")
