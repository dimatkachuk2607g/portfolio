"""
Tests for the form Page Object, asserting every method and form functionality
"""

def test_text(form_page):
    assert "Form" in form_page.get_title()
    assert "Automation" in form_page.get_header()

def test_click_homepage_link(form_page):
    form_page.click_homepage_link()
    assert "Homepage" in form_page.get_title()

def test_form_success(form_page):
    form_page.enter_firstname("Arnold")
    form_page.enter_lastname("Schwarzenegger")
    form_page.enter_password("abcd1234")
    form_page.enter_email("abcd@email.com")
    form_page.enter_age("70")
    form_page.select_country("uk")
    form_page.radio_button_female()
    form_page.radio_button_male()
    form_page.checkbox_gaming()
    form_page.checkbox_coding()

    alert = form_page.submit_alert()
    assert "success" in alert.text
    alert.accept()