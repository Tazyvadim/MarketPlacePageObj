from locators import CountryAlertLocators
from ..BasePage import BasePage


class CountryAlert(BasePage):

    def get_title(self, number):
        index = number - 1
        return self._get_element_text(CountryAlertLocators.title_country, index=index)

    def access_country(self, title, number):
        index = number - 1
        if title == 'Ваша страна?':
            self._click(CountryAlertLocators.access, index= index)
        elif title == 'Выберите свою страну':
            self._click(CountryAlertLocators.choise_country, index= index)