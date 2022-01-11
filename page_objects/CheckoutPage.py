from locators import CheckoutLocators
from .BasePage import BasePage

class CheckoutPage(BasePage):
    def select_country(self, number):
        index = number -1
        self._wait_for_visible(CheckoutLocators.country)
        self._click(CheckoutLocators.country, index)

    def select_delivery_method(self, number):
        index = number - 1
        self._wait_for_visible(CheckoutLocators.delivery_method)
        self._click(CheckoutLocators.country, index)