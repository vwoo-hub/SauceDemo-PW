from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.locator(".submit-button")
        self.error_message_label = page.locator('.error-message-container')

    def type_username_field(self, username):
        self.username_field.fill(username)

    def type_password_field(self, password):
        self.password_field.fill(password)

    def tap_login_button(self):
        self.login_button.click()

    def login_success(self, username, password):
        self.type_username_field(username)
        self.type_password_field(password)
        self.tap_login_button()