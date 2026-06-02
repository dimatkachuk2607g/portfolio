from playwright.sync_api import Page


class DemoPage():
    def __init__(self, page:Page):
        self.page = page

    def checkboxes_url(self):
        return self.page.get_by_role("link", name="Checkboxes")

    def checkbox_1(self):
        return self.page.locator("#checkboxes input[type='checkbox']").nth(0)

    def checkbox_2(self):
        return self.page.locator("#checkboxes input[type='checkbox']").nth(1)

