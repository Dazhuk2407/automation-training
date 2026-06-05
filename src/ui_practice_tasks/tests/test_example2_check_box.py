"""
Task 02 — Check Box
URL: https://demoqa.com/checkbox
"""

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import logging 



URL = "https://demoqa.com/checkbox"
log = logging.getLogger("test_checkbox_selection_shows_result")

def test_checkbox_selection_shows_result():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ===== Arrange =====
        page.goto(URL)
        log.info("Page loaded")
        
        #page.pause()
    
        # ===== Act =====
        # Розгорнути все дерево одним кліком:
        page.locator('.rc-tree-switcher').click()
        #page.locator('button[title="Expand all"]').click()

        # TODO: клікнути по чекбоксу ноди Desktop
        page.get_by_label("Select Desktop").check()
        #page.get_by_role("Select Desktop").click()
        #page.locator('span.rc-tree-checkbox[aria-label="Select Desktop"]').click()


        # ===== Assert =====
        # Дочекатися появи блоку результату:
        page.locator("#result").wait_for(state="visible")

        # TODO: assert що блок #result видимий
        # Підказка: assert page.locator("#result").is_visible()
        assert page.locator("#result").is_visible()

        # TODO: assert що рядок "desktop" є у тексті #result
        # Підказка: assert "desktop" in page.locator("#result").text_content()
        assert "desktop" in page.locator('#result').text_content()
        expect(page.locator('#result')).to_contain_text("desktop")


        # TODO: assert що інпут #tree-node-desktop у стані checked
        # Підказка: метод .is_checked()
        assert page.locator('span.rc-tree-checkbox[aria-label="Select Desktop"]').is_checked()
        
        browser.close()