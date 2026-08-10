from playwright.sync_api import Page
from playwright.sync_api import sync_playwright



class HomePage:
    def __init__(self, page: Page):
        self.page = page        
        self.locator_elements_card = page.locator(".card-body", has_text="Elements")


    def click_elements_card_verify_URL(self):
        self.locator_elements_card.click()

# verify by URL
# add URL in config file
# add verification in method