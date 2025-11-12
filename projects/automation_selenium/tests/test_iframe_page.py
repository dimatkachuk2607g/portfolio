"""
Tests for the iframe Page Object
asserting every method and iframe functionality
"""

def test_text(iframe_page):
    assert "iframe" in iframe_page.get_title()
    assert "Automation" in iframe_page.get_header()

def test_click_homepage_link(iframe_page):
    iframe_page.click_homepage_link()
    assert "Homepage" in iframe_page.get_title()

def test_radio_button_a_selected(iframe_page):
    iframe_page.radio_button_a()
    assert iframe_page.radio_button_a_selected()

def test_radio_button_b_selected(iframe_page):
    iframe_page.radio_button_b()
    assert iframe_page.radio_button_b_selected()

def test_iframe_checkbox_button(iframe_page):
    iframe_page.iframe_checkbox_button()
    assert iframe_page.iframe_checkbox_button_selected()