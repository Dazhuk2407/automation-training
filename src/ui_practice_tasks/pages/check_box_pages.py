from playwright.sync_api import Page


class CheckBoxPages:
    def __init__(self, page: Page):
        self._page = page

        self.locator_extend_tree= page.locator('.rc-tree-switcher')
        self.locator_result= page.locator("#result")

    def expand_tree(self):
        self.locator_extend_tree.click()

    def click_desktop_checkbox(self):
        self._page.get_by_label("Select Desktop").check()

    def is_result_visible(self):
        return self.locator_result.is_visible()

    def has_desktop_in_result(self):
        return "desktop" in self.locator_result.text_content()  
    
    def is_desktop_checkbox_checked(self):
        return self._page.locator('span.rc-tree-checkbox[aria-label="Select Desktop"]').is_checked()


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
