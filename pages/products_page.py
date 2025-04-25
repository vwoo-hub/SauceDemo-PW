import pytest
from playwright.sync_api import expect, Page

from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.backpack_add_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.bike_light_add_button = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.shirt_add_button = page.locator("#add-to-cart-sauce-labs-bolt-t-shirt")
        self.jacket_add_button = page.locator('#add-to-cart-sauce-labs-fleece-jacket')
        self.onesie_add_button = page.locator("#add-to-cart-sauce-labs-onesie")
        self.red_shirt_add_button = page.locator('add-to-cart-test.allthethings()-t-shirt-(red)')

        self.backpack_remove_button = page.locator("#remove-sauce-labs-backpack")
        self.bike_light_remove_button = page.locator("#remove-sauce-labs-bike-light")
        self.shirt_remove_button = page.locator("#remove-sauce-labs-bolt-t-shirt")
        self.jacket_remove_button = page.locator('#remove-sauce-labs-fleece-jacket')
        self.onesie_remove_button = page.locator("#remove-sauce-labs-onesie")
        self.red_shirt_remove_button = page.locator('#remove-test.allthethings()-t-shirt-(red)')


    def tap_add_product_button(self, product):
        match product:
            case "backpack":
                self.backpack_add_button.click()
            case "bike light":
                self.bike_light_add_button.click()
            case "shirt":
                self.shirt_add_button.click()
            case "jacket":
                self.jacket_add_button.click()
            case "onesie":
                self.onesie_add_button.click()
            case "red shirt":
                self.red_shirt_add_button.click()
            case _:
                raise ValueError(f"Unknown product: {product}")
