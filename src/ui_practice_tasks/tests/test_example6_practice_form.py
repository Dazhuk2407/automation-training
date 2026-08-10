"""
Task 06 — Practice Form
URL: https://demoqa.com/automation-practice-form
"""


def test_practice_form_submission_shows_modal_with_correct_data(practice_form_page):
        first_name = "John"
        last_name = "Carton"
        email = "john.carton@example.com"
        mobile = "1234567890"
        address = "123 Main St"

        practice_form_page.fill_form(
            first_name=first_name, 
            last_name=last_name,
            email=email,
            mobile=mobile,
            address=address
        )
        practice_form_page.submit_form()
        practice_form_page.wait_for_modal()

        assert practice_form_page.has_title()
        assert practice_form_page.has_full_name_in_modal(first_name, last_name)
        assert practice_form_page.has_email_in_modal(email)
        assert practice_form_page.has_mobile_in_modal(mobile)