"""
Page Object for automating the iframe page, reads text and verifies the iframe is working correctly
"""

from selenium.webdriver.common.by import By


class IFrame:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.header = (By.TAG_NAME, "h1")
        self.homepage_link = (By.LINK_TEXT, "Home page")
        self.radio_btn_a = (By.XPATH, "//input[@value='A']")
        self.radio_btn_b = (By.XPATH, "//input[@value='B']")
        self.iframe_window = (By.ID, "practiceIframe")
        self.iframe_checkbox = (By.ID, "iframeCheckbox")


    def get_title(self):
        return self.driver.title

    def get_header(self):
        return self.driver.find_element(*self.header).text

    def click_homepage_link(self):
        self.driver.find_element(*self.homepage_link).click()

    def radio_button_a(self):
        self.driver.find_element(*self.radio_btn_a).click()

    def radio_button_a_selected(self):
        return self.driver.find_element(*self.radio_btn_a).is_selected()

    def radio_button_b(self):
        self.driver.find_element(*self.radio_btn_b).click()

    def radio_button_b_selected(self):
        return self.driver.find_element(*self.radio_btn_b).is_selected()

    def iframe_checkbox_button(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.iframe_window))
        self.driver.find_element(*self.iframe_checkbox).click()
        self.driver.switch_to.default_content()

    def iframe_checkbox_button_selected(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.iframe_window))
        is_selected = self.driver.find_element(*self.iframe_checkbox).is_selected()
        self.driver.switch_to.default_content()
        return is_selected


