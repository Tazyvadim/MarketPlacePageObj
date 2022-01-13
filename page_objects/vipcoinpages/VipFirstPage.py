from ..BasePage import BasePage
from locators.vipcoinlocators import FirstVippageLocators


class VipFirstPage(BasePage):

    def get_payment_amount(self):
        self._get_element_text(FirstVippageLocators.Paymant_amaount)

    def select_type_of_pay(self, number):
        index = number - 1
        self._click(FirstVippageLocators.type_of_pay_list, index= index)
