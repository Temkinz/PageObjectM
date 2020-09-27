from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        assert self.should_be_login_url() == True, "Login link is not presented"
        assert self.should_be_login_form() == True, "Login form is not presented"
        assert self.should_be_register_form() == True, "Register form is not presented"

    def should_be_login_url(self):
        current_url = self.current_url()
        assert "login" in current_url.text, "Login link is not presented"

    def should_be_login_form(self):
        self.is_element_present(*MainPageLocators.LOGIN_FORM)
        assert True, "Login form is not presented"

    def should_be_register_form(self):
        self.is_element_present(*MainPageLocators.REGISTER_FORM)
        assert True, "Register form is not presented"