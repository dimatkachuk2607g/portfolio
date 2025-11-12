"""
Tests for the form Page Object
asserting every method and form functionality
"""

from playwright.sync_api import expect, Dialog


def test_title(form_page):
    expect(form_page.title()).to_have_title("Form")

def test_header(form_page):
    expect(form_page.header()).to_be_visible()

def test_homepage_link(form_page):
    form_page.homepage_link().click()
    expect(form_page.title()).to_have_title("Automation Practice Homepage")

def test_form(form_page):
    form_page.firstname().fill("Arnold")
    form_page.lastname().fill("Schwarzenegger")
    form_page.password().fill("abcd1234")
    form_page.email().fill("abcd@email.com")
    form_page.age().fill("70")
    form_page.select_country().select_option("uk")
    form_page.radio_button_female().click()
    form_page.radio_button_male().click()
    form_page.checkbox_coding().click()
    form_page.checkbox_gaming().click()

    # Test alert message to make sure form was successfully submitted
    alert_text = None
    def alert_popup(dialog:Dialog):
        nonlocal alert_text
        alert_text = dialog.message
        dialog.accept()

    form_page.page.once("dialog", alert_popup)
    form_page.submit_button().click()
    assert alert_text == "Form submitted successfully"

