import time

from locators import CheckoutLocators
from .BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CheckoutPage(BasePage):
    def select_country(self, number):
        index = number - 1
        time.sleep(5)
        self._click(CheckoutLocators.country, index)

    def select_first_delivery_method(self, number):
        time.sleep(5)
        index = number - 1
        self._click(CheckoutLocators.firts_delivery_method, index)

    def select_second_delivery_method(self):
        self._click(CheckoutLocators.second_delivery_method)

    def select_third_delivery_method(self):
        self._wait_for_visible(CheckoutLocators.third_delivery_method)
        self._click(CheckoutLocators.third_delivery_method)

    def vipvip_button(self):
        self._wait_for_visible(CheckoutLocators.vipvip_button)
        self._click(CheckoutLocators.vipvip_button)