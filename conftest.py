import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def set_up(page: Page):
    page.goto("https://www.saucedemo.com/")
