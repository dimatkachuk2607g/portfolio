"""
Page Object for automating the form page
defines all the locators and methods to use them through tests
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class FormPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.header = (By.TAG_NAME, "h1")
        self.homepage_link = (By.LINK_TEXT, "Home page")
        self.firstname = (By.ID, "firstname")
        self.lastname = (By.ID, "lastname")
        self.password = (By.ID, "password")
        self.email = (By.ID, "email")
        self.age = (By.ID, "age")
        self.country = (By.ID, "country")
        self.radio_male = (By.CSS_SELECTOR, "input[value='male']")
        self.radio_female = (By.XPATH, "//input[@value='female']")
        self.checkb_coding = (By.ID, "coding")
        self.checkb_gaming = (By.ID, "gaming")
        self.alert_button = (By.CSS_SELECTOR, "input[type='submit']")


    def get_title(self):
        return self.driver.title

    def get_header(self):
        return self.driver.find_element(*self.header).text

    def click_homepage_link(self):
        self.driver.find_element(*self.homepage_link).click()

    def enter_firstname(self, text):
        self.driver.find_element(*self.firstname).send_keys(text)

    def enter_lastname(self, text):
        self.driver.find_element(*self.lastname).send_keys(text)

    def enter_password(self, text):
        self.driver.find_element(*self.password).send_keys(text)

    def enter_email(self, text):
        self.driver.find_element(*self.email).send_keys(text)

    def enter_age(self, text):
        self.driver.find_element(*self.age).send_keys(text)

    def select_country(self, text):
        Select(self.driver.find_element(*self.country)).select_by_value(text)

    def radio_button_male(self):
        self.driver.find_element(*self.radio_male).click()

    def radio_button_female(self):
        self.driver.find_element(*self.radio_female).click()

    def checkbox_coding(self):
        self.driver.find_element(*self.checkb_coding).click()

    def checkbox_gaming(self):
        self.driver.find_element(*self.checkb_gaming).click()

    def submit_alert(self):
        self.driver.find_element(*self.alert_button).click()
        alert = self.driver.switch_to.alert
        return alert


