from .base_page import BasePage
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
import math

class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BUTTON)
        add_button.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    from selenium.common.exceptions import NoAlertPresentException  # в начале файла

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    #def should_be_product_in_cart(self):
