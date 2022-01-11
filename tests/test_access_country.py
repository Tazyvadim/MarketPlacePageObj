import time
from page_objects import CountryAlertPage, MainPage, ProductPage, LoginAlertPage, CheckoutPage
from page_objects.common import Header
from page_objects.common import SiteBar
import json

with open('passw_data.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']


def test_access_country(browser):
    CountryAlertPage(browser).wait_element()
    CountryAlertPage(browser).access_country()
    MainPage(browser).select_product(2)
    ProductPage(browser).add_to_cart()
    time.sleep(5)
    Header(browser).go_to_cart()
    time.sleep(5)
    SiteBar(browser).go_to_checkout()
    time.sleep(5)
    LoginAlertPage(browser).login_user(email=login, password=password)
    time.sleep(5)
    CheckoutPage(browser).select_country(1)
    CheckoutPage(browser).select_delivery_method(3)
    time.sleep(5)
