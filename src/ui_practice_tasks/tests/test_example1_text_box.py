"""
Task 01 — Text Box
URL: https://demoqa.com/text-box
"""


def test_text_box_submission_displays_submitted_data(text_box_page):
        full_name = "John Carton"
        email = "john.carton@example.com"
        current_address = "123 Main St"
        permanent_address = "456 Other St"

        text_box_page.fill_text_box_form(
                full_name=full_name,
                email=email,
                current_address=current_address,
                permanent_address=permanent_address
        )
        text_box_page.submit_form()
        text_box_page.is_output_block_visible()
        text_box_page.has_full_name_in_output(full_name)
        text_box_page.has_email_in_output(email)
        text_box_page.has_current_address_in_output(current_address)
        text_box_page.has_permanent_address_in_output(permanent_address)