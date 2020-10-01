from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_MESSAGE_ACTUAL = (By.CSS_SELECTOR, "div.alert-success > div")
    REGISTRATION_MESSAGE_EXPECTED = "Thanks for registering!"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*self.LOGIN_LINK), "Login link is not presented"

    def check_registration_message(self):
        registration_message = self.browser.find_element(*self.REGISTRATION_MESSAGE_ACTUAL).text
        assert self.REGISTRATION_MESSAGE_EXPECTED in registration_message, f"expected {self.REGISTRATION_MESSAGE_EXPECTED}, got {registration_message}"

