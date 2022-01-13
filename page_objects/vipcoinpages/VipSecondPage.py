from ..BasePage import BasePage
from locators.vipcoinlocators import SecondVippageLocators


class VipSecondPage(BasePage):

    def get_payment_amount(self):
        self._get_element_text(SecondVippageLocators.Paymant_amaount)

    def upload_keyfile(self, file):
        self._upload_file(SecondVippageLocators.upload_keyfile_button, file)

    def enter_password(self , password):
        self._wait_for_visible(SecondVippageLocators.password_input)
        self._input(SecondVippageLocators.password_input, password)

    def show_wallets(self):
        self._click(SecondVippageLocators.show_wallets_button)

    def confirm_withdrawal(self):
        self._click(SecondVippageLocators.confirm_withdrawal_button)

    def pay(self):
        self._wait_for_clickable(SecondVippageLocators.pay_button)
        self._click(SecondVippageLocators.pay_button)