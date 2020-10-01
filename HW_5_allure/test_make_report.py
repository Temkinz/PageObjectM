from .pages.main_page import MainPage
from .pages.utils import Utils
from faker import Faker

fake = Faker()


def test_user_can_be_registered(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
    email = fake.email()
    password = Utils.passwords()
    login_page.register(email, password)
    login_page = MainPage(browser, link)
    login_page.check_registration_message()


