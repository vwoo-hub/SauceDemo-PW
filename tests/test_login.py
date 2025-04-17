import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


class TestLogin:
    @pytest.fixture(autouse=True)
    def set_up_pages(self, page):
        self.login_page = LoginPage(page)

    def test_login_valid_user(self):
        self.login_page.type_username_field('standard_user')
        self.login_page.type_password_field('secret_sauce')
        self.login_page.tap_login_button()

        assert 'inventory' in self.login_page.page.url


    def test_login_locked_out_user(self):
        error_message = 'Epic sadface: Sorry, this user has been locked out.'

        self.login_page.type_username_field('locked_out_user')
        self.login_page.type_password_field('secret_sauce')
        self.login_page.tap_login_button()

        expect(self.login_page.error_message_label).to_have_text(error_message)
