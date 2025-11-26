"""
Page Object for automating the iframe page,
defines all the locators and methods to use them through tests
"""

from playwright.sync_api import Page


class IFrame:
    def __init__(self, page:Page):
        self.page = page

    def header(self):
        return self.page.get_by_text("Practice iframe Automation")

    def homepage_link(self):
        return self.page.get_by_role("link", name="Home page")

    def radio_button_a(self):
        return self.page.locator("input[value='A']")

    def radio_button_b(self):
        return self.page.locator("input[value='B']")

    def iframe_checkbox(self):
        return self.page.frame_locator("#practiceIframe").locator("#iframeCheckbox")
