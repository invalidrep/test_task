from .base_page import BasePage

class BuilderPage(BasePage):
    CANVAS_SELECTOR = "//canvas[@id='unity-app-canvas']"
    LOGOUT_BTN = "//p[text()='Log Out']"
    OK_BTN = "//button[text()='Ok']"
    IFRAME_SELECTOR = "//iframe"
    ACCOUNT_AVATAR = "(//img[@role='img'])[1]"
    LOGOUT_CONF_BTN = "//button[text()='Log Out']"

    def wait_for_canvas(self):
        self.wait_for(self.CANVAS_SELECTOR, frame_selector=self.IFRAME_SELECTOR)

    def skip_limited_tablet(self):
        self.click(self.OK_BTN)

    def logout(self):
        self.click_account_avatar()
        self.click(self.LOGOUT_BTN)
        self.click(self.LOGOUT_CONF_BTN)

    def click_account_avatar(self):
        self.click(self.ACCOUNT_AVATAR)

