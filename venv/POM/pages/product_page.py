from .base_page import BasePage
from selenium.webdriver.common.by import By
import math


class ProductPage(BasePage):
    PRODUCT_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, "div h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    BOOK_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages p:nth-child(1) > strong")

    def add_product_to_cart(self):
        add_button = self.browser.find_element(*self.PRODUCT_ADD_BUTTON).click()

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

    #def get_book_title(self):
        #book_title = self.browser.find_element(*self.BOOK_TITLE).text
        #return book_title

    #def get_price(self):
        #price = self.browser.find_element(*self.PRICE).text
        #return price

    #def get_book_message(self):
        #book_message = self.browser.find_element(*self.BOOK_MESSAGE).text
        #return book_message

    #def get_price_message(self):
        #price_message = self.browser.find_element(*self.PRICE_MESSAGE).text
        #return price_message

    def should_be_product_in_cart(self):
        assert self.browser.find_element(*self.BOOK_TITLE).text in self.browser.find_element(*self.BOOK_MESSAGE).text

    def should_be_correct_price(self):
        assert self.browser.find_element(*self.PRICE).text in self.browser.find_element(*self.PRICE_MESSAGE).text
