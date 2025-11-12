"""
Tests for the index Page Object
asserting every method and link to have the correct information
"""

def test_text(index_page):
    assert "Automation" in index_page.get_title()
    assert "Basic" in index_page.get_header_text()
    assert "Welcome" in index_page.get_paragraph_text()

def test_form_link(index_page):
    index_page.click_form_link()
    assert "Form" in index_page.get_title()

def test_iframe_link(index_page):
    index_page.click_iframe_link()
    assert "iframe" in index_page.get_title()
