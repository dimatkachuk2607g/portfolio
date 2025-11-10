"""
Page Object for automating the Index page, reads text and verifies all links on the page
"""

from selenium.webdriver.common.by import By

class IndexPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.header_text = (By.TAG_NAME, "h1")
        self.paragraph_text = (By.TAG_NAME, "p")
        self.form_link = (By.LINK_TEXT, "Form Page")
        self.frame_link = (By.LINK_TEXT, "iframe Page")


    def get_title(self):
        return self.driver.title

    def get_header_text(self):
        return self.driver.find_element(*self.header_text).text

    def get_paragraph_text(self):
        return self.driver.find_element(*self.paragraph_text).text

    def click_form_link(self):
        self.driver.find_element(*self.form_link).click()

    def click_iframe_link(self):
        self.driver.find_element(*self.frame_link).click()










