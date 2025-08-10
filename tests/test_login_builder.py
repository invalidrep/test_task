from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.builder_page import BuilderPage

BASE_URL = "https://events.shooters.global/"
EMAIL = "vagef28371@ahvin.com"
PASSWORD = "22VhY9o00m"

def test_login_and_builder(page):
    home = HomePage(page)
    login = LoginPage(page)
    builder = BuilderPage(page)

    home.goto(BASE_URL)
    home.click_build_for_free()
    assert login.is_loaded(), "Login page is not loaded"

    login.login(EMAIL, PASSWORD)
    builder.skip_limited_tablet()
    assert login.is_logged_in(), "User did not log in"

    builder.wait_for_canvas()

    builder.logout()
    assert home.is_logged_out("https://events.shooters.global/"), "User did not log out"