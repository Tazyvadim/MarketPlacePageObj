from .BasePage import BasePage
from locators import CountryAlert


class CountryAlertPage(BasePage):
    def wait_element(self):
        self._wait_for_visible(CountryAlert.country)

    def access_country(self):
        self._click(CountryAlert.access)

    def get_text(self):
        return self._get_element_text(CountryAlert.country)
