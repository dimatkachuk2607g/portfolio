"""
Tests for the iframe Page Object
asserting every method and iframe functionality
"""

from playwright.sync_api import expect

def test_title(iframe_page):
    expect(iframe_page.page).to_have_title("iframe")

def test_header(iframe_page):
    expect(iframe_page.header()).to_be_visible()
    
def test_homepage_link(iframe_page):
    iframe_page.homepage_link().click()
    expect(iframe_page.page).to_have_title("Automation Practice Homepage")

def test_radio_button_a(iframe_page):
    iframe_page.radio_button_a().click()
    expect(iframe_page.radio_button_a()).to_be_checked()

def test_radio_button_b(iframe_page):
    iframe_page.radio_button_b().click()
    expect(iframe_page.radio_button_b()).to_be_checked()

def test_iframe_checkbox(iframe_page):
    iframe_page.iframe_checkbox().click()
    expect(iframe_page.iframe_checkbox()).to_be_checked()

