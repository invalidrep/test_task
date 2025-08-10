from .base_page import BasePage

class HomePage(BasePage):
    BUILD_FOR_FREE_BTN = "(//button[text()='Build for free'])[1]"
    LOGGED_OUT_BANNER = "//li[@title='Logged Out!']"

    def click_build_for_free(self):
        self.click(self.BUILD_FOR_FREE_BTN)

    def is_logged_out(self, expected_url: str) -> bool:
        banner_visible = self.page.is_visible(self.LOGGED_OUT_BANNER)
        url_matches = self.page.url == expected_url
        return banner_visible and url_matches