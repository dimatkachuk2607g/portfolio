"""
Shared pytest fixtures for selenium pages to avoid repetitive driver and object creation
"""

import pytest
from selenium import webdriver
from pathlib import Path
from automation_selenium.pages.form_page import FormPage
from automation_selenium.pages.iframe_page import IFrame
from automation_selenium.pages.index_page import IndexPage


@pytest.fixture(scope="function")
def driver():
    """driver initialization
    Headless Mode: remove comment tags from the options below and
    add options=options as argument to driver = webdriver.Chrome()
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def index_page(driver):
    """Create an IndexPage Object to be shared across tests"""
    index_page_path = Path(__file__).parent.parent.parent / "basic_website" / "src" / "index.html"
    index_html_url = index_page_path.resolve().as_uri()
    driver.get(index_html_url)
    return IndexPage(driver)

@pytest.fixture(scope="function")
def form_page(driver):
    """Create a FormPage Object to be shared across tests"""
    form_page_path = Path(__file__).parent.parent.parent / "basic_website" / "src" / "form.html"
    form_html_url = form_page_path.resolve().as_uri()
    driver.get(form_html_url)
    return FormPage(driver)

@pytest.fixture(scope="function")
def iframe_page(driver):
    """Create an IFrame Object to be shared across tests"""
    iframe_page_path = Path(__file__).parent.parent.parent / "basic_website" / "src" / "iframe.html"
    iframe_html_url = iframe_page_path.resolve().as_uri()
    driver.get(iframe_html_url)
    return IFrame(driver)