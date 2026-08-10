"""
Task 03 — Radio Button
URL: https://demoqa.com/radio-button
"""

def test_radio_button_selects_yes_and_no_is_disabled(radio_button_page):
    
    radio_button_page.click_by_yes_radio()

    assert radio_button_page.is_yes_radio_checked()
    assert "Yes" in radio_button_page.locator_text_success.text_content()
    assert radio_button_page.is_no_radio_disabled()