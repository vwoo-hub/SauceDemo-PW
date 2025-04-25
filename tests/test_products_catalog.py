from time import sleep

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestProductsCatalog:
    @pytest.fixture(autouse=True)
    def set_up_pages(self, page):
        self.login_page = LoginPage(page)
        self.products_page = ProductsPage(page)

    def test_add_product_to_cart(self):
        self.login_page.login_success("standard_user", "secret_sauce")

        self.products_page.tap_add_product_button("shirt")

        expect(self.products_page.shirt_remove_button).to_be_visible()