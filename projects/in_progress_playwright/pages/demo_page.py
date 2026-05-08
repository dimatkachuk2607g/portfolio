from playwright.sync_api import Page

class DemoPage():
    def __init__(self, page:Page):
        self.page = page

    def checkboxes_url(self):
        return self.page.get_by_text("Checkboxes")


