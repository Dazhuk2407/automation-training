"""
Task 02 — Check Box
URL: https://demoqa.com/checkbox
"""


def test_checkbox_selection_shows_result(check_box_page):
        check_box_page.expand_tree()
        check_box_page.click_desktop_checkbox()

        assert check_box_page.is_result_visible()
        assert check_box_page.has_desktop_in_result()
        assert check_box_page.is_desktop_checkbox_checked()