from locators import MainPageLocators
from .BasePage import BasePage

class MainPage(BasePage):

    def first_product(self):
        self._click(MainPageLocators.first_product)