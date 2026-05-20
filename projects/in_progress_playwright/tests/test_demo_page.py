from playwright.sync_api import expect


def test_title(demo_page):
    expect(demo_page.page).to_have_title("The Internet")
    

def test_checkboxes_url(demo_page):
    demo_page.checkboxes_url().click()
    expect(demo_page.page).to_have_title("The Internet")
    

def test_checkbox_1(demo_page):
    demo_page.checkboxes_url().click()
    expect(demo_page.checkbox_1()).not_to_be_checked()
    demo_page.checkbox_1().click()
    expect(demo_page.checkbox_1()).to_be_checked()
    