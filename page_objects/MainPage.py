from locators import MainPageLocators
from .BasePage import BasePage


class MainPage(BasePage):

    def select_product(self, number):
        index = number - 1
        self._click(MainPageLocators.product, index=index)
