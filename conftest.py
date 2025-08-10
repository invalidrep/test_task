import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p

@pytest.fixture
def browser(pw):
    browser = pw.chromium.launch(headless=False, slow_mo=50)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()