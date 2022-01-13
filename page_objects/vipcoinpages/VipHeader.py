from ..BasePage import BasePage
from locators.vipcoinlocators import VipHeaderLocators

class VipHeader(BasePage):

    def open_lang(self, number):
        index = number - 1
        self._click(VipHeaderLocators.open_lang, index=index)

    def select_lang(self, number):
        index = number - 1
        self._click(VipHeaderLocators.list_of_lang, index = index)