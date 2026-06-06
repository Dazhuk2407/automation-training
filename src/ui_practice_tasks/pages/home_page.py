from playwright.sync_api import Page
from enum import Enum
from ui_practice_tasks.pages.web_tables_pages import WebTablesPages



class PageElements(Enum):
    LINK_ELEMENTS= "elements"
    LINK_FORMS  = "forms"
    LINK_WIDGETS = "widgets"
    LIST_TEXT_BOX_ = "Text Box"
    LIST_WEB_TABLES = "Web Tables"


class HomePage:
    def __init__(self, page: Page):
        self._page = page

        self.elements_card = page.locator("h5",
                                          has_text=PageElements.LINK_ELEMENTS.value)
        self.web_tables_item = page.locator("span",
                                            has_text=PageElements.LIST_WEB_TABLES.value)

    def open_web_tables_page(self):
        self.elements_card.click()
        self.web_tables_item.click()
        self._page.wait_for_url("**/webtables")

        return WebTablesPages(self._page)
