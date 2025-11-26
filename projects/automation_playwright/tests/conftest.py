"""
Shared pytest fixtures for playwright pages to avoid repetitive driver and object creation
"""

import pytest
from playwright.sync_api import Page
from pathlib import Path
from automation_playwright.pages.form_page import FormPage
from automation_playwright.pages.iframe_page import IFrame
from automation_playwright.pages.index_page import IndexPage


@pytest.fixture(scope="function")
def index_page(page:Page):
    """Create an IndexPage Object to be shared across tests"""
    index_page_path = Path(__file__).parent.parent.parent / "basic_website" / "src" / "index.html"
    index_html_url = index_page_path.resolve().as_uri()
    page.goto(index_html_url)
    return IndexPage(page)

@pytest.fixture(scope="function")
def form_page(page:Page):
    """Create a FormPage Object to be shared across tests"""
    form_page_path = Path(__file__).parent.parent.parent / "basic_website" / "src" / "form.html"
    form_html_url = form_page_path.resolve().as_uri()
    page.goto(form_html_url)
    return FormPage(page)

@pytest.fixture(scope="function")
def iframe_page(page:Page):
    """Create an IFrame Object to be shared across tests"""
    iframe_page_path = Path(__file__).parent.parent.parent / "basic_website" / "src" / "iframe.html"
    iframe_html_url = iframe_page_path.resolve().as_uri()
    page.goto(iframe_html_url)
    return IFrame(page)