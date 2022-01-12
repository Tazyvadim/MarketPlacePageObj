import time
from page_objects import MainPage, ProductPage, CheckoutPage, LoginAlertPage
from page_objects.common import Header, CountryAlert
from page_objects.common import SiteBar
import json

with open('passw_data.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']


def test_access_country(browser):
    # CountryAlertPage(browser).wait_element()
    title = CountryAlert(browser).get_title(1)
    CountryAlert(browser).access_country(title, 1)
    MainPage(browser).select_product(2)
    ProductPage(browser).add_to_cart()
    Header(browser).go_to_cart()
    SiteBar(browser).go_to_checkout()
    LoginAlertPage(browser).login_user(email=login, password=password)
    CheckoutPage(browser).select_country(1)
    CheckoutPage(browser).select_first_delivery_method(1)
    CheckoutPage(browser).vipvip_button()
