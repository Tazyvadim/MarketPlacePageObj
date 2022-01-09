from .BasePage import BasePage
from locators import LoginAlertLocators


class LoginAlertPage(BasePage):

    def login_user(self, email, password):
        self._input(LoginAlertLocators.login_field, email)
        self._input(LoginAlertLocators.password_field, password)
        self._click(LoginAlertLocators.button_login)