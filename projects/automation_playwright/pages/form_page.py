"""
Page Object for automating the form page
defines all the locators and methods to use them through tests
"""

from playwright.sync_api import Page


class FormPage:
    def __init__(self, page:Page):
        self.page = page

    def header(self):
        return self.page.get_by_text("Practice Filling Forms Automation")

    def homepage_link(self):
        return self.page.get_by_role("link", name="Home page")

    def firstname(self):
        return self.page.get_by_label("First Name:")

    def lastname(self):
        return self.page.get_by_label("Last Name:")

    def password(self):
        return self.page.get_by_label("Password:")

    def email(self):
        return self.page.get_by_label("Email:")

    def age(self):
        return self.page.get_by_label("Age:")

    def select_country(self):
        return self.page.get_by_label("Country:")

    def radio_button_male(self):
        return self.page.locator("#male")

    def radio_button_female(self):
        return self.page.locator("#female")

    def checkbox_gaming(self):
        return self.page.get_by_label("Gaming")

    def checkbox_coding(self):
        return self.page.get_by_label("Coding")

    def submit_button(self):
        return self.page.get_by_role("button", name="Submit Form")