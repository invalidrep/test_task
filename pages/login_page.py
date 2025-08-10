from .base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    EMAIL_INPUT = "//input[@name='emailOrPhoneNumber']"
    PASSWORD_INPUT = "//input[@name='password']"
    SIGNIN_BTN = "//button[@type='submit']"
    SIGN_IN_TITLE = "//h3[@class='text-2xl font-semibold md:text-3xl']"
    LOGGED_IN_BANNER = "//li[@title='Logged In']"

    def login(self, email, password):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.SIGNIN_BTN)

    def is_loaded(self):
        try:
            expect(self.page.locator(self.SIGN_IN_TITLE)).to_be_visible(timeout=5000)
            return True
        except TimeoutError:
            return False

    def is_logged_in(self):
        try:
            expect(self.page.locator(self.LOGGED_IN_BANNER)).to_be_visible(timeout=5000)
            return True
        except TimeoutError:
            return False


