from .pages.main_page import MainPage
from .pages.utils import Utils


def test_user_can_be_registered(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
    email = Utils.email()
    password = Utils.passwords()
    login_page.register(email, password)
    login_page = MainPage(browser, browser.current_url)
    login_page.check_registration_message()


