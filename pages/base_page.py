class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.fill(locator, text)

    def wait_for(self, locator, frame_selector=None):
        if frame_selector:
            self.page.frame_locator(frame_selector).locator(locator).wait_for(state="visible")
        else:
            self.page.wait_for_selector(locator, state="visible")