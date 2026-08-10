"""
Task 04 — Buttons
URL: https://demoqa.com/buttons
"""



def test_buttons_double_right_and_single_click_messages(buttons_page):
    
    buttons_page.click_by_double_click_btn()
    buttons_page.click_by_right_click_btn()
    buttons_page.click_by_dynamic_click_btn()

    assert buttons_page.has_double_click_message()
    assert buttons_page.has_right_click_message()
    assert buttons_page.has_dynamic_click_message()