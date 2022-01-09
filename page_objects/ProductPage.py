from .BasePage import BasePage
from locators import ProductPageLocators

class ProductPage(BasePage):
    # def wait_element(self, number):
    #     index = number - 1
    #     self._wait_for_visible(CountryAlert.country, index=index)
    #
    # def get_text(self, number):
    #     index = number - 1
    #     return self._get_element_text(CountryAlert.country, index=index)

    def add_to_cart(self):
        self._wait_for_visible(ProductPageLocators.add_to_card)
        return self._click(ProductPageLocators.add_to_card)