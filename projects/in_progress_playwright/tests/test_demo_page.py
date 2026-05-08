from playwright.sync_api import expect
import time

def test_title(demo_page):
    expect(demo_page.page).to_have_title("The Internet")
    time.sleep(2)

def test_checkboxes_url(demo_page):
    demo_page.checkboxes_url().click()
    expect(demo_page.page).to_have_title("The Internet")
    time.sleep(2)