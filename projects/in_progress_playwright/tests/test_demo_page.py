from playwright.sync_api import expect
import time

def test_title(demo_page):
    expect(demo_page.page).to_have_title("The Internet")
    time.sleep(2)