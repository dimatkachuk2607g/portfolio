"""
Tests for the index Page Object
asserting every method and link to have the correct information
"""

from playwright.sync_api import expect


def test_title(index_page):
    expect(index_page.page).to_have_title("Automation Practice Homepage")

def test_header(index_page):
    expect(index_page.header()).to_be_visible()

def test_paragraph(index_page):
    expect(index_page.paragraph()).to_be_visible()

def test_form_link(index_page):
    index_page.form_link().click()
    expect(index_page.page).to_have_title("Form")

def test_iframe_link(index_page):
    index_page.iframe_link().click()
    expect(index_page.page).to_have_title("iframe")




