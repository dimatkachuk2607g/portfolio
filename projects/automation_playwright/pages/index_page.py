"""
Page Object for automating the Index page
defines all the locators and methods to use them through tests
"""

from playwright.sync_api import Page


class IndexPage:
    def __init__(self, page:Page):
        self.page = page

    def title(self):
        return self.page

    def header(self):
        return self.page.get_by_role("heading", name="Basic Website for Automation")

    def paragraph(self):
        return self.page.get_by_text("Welcome to my")

    def form_link(self):
        return self.page.get_by_role("link" ,name="Form Page")

    def iframe_link(self):
        return self.page.get_by_role("link" ,name="iframe Page")