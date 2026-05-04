import pytest
from playwright.sync_api import Page
from in_progress_playwright.pages.demo_page import DemoPage

@pytest.fixture(scope="function")
def demo_page(page:Page):
    page.goto("https://the-internet.herokuapp.com/")
    return DemoPage(page)



