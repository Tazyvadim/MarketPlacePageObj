import time
import json
import os
from page_objects import MainPage, ProductPage, CheckoutPage, LoginAlertPage
from page_objects.common import Header, CountryAlert, SiteBar
from page_objects.vipcoinpages import VipSecondPage, VipFirstPage

with open('passw_data.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']
    password_for_key = data['password_for_key']


def test_access_country(browser):
    # Выбор страны локализации
    title = CountryAlert(browser).get_title(1)
    CountryAlert(browser).access_country(title, 1)
    # Выбор продукта - индекс -> номер продукта в блоке популярные товары
    MainPage(browser).select_product(2)
    # product_name = ProductPage(browser).get_product_name()
    # Добавление товара в корзину
    ProductPage(browser).add_to_cart()
    Header(browser).go_to_cart()
    SiteBar(browser).go_to_checkout()
    # Авторизация
    LoginAlertPage(browser).login_user(email=login, password=password)
    time.sleep(4)
    # Выбор способа доставки в чекауте
    # checkout_product_name = CheckoutPage(browser).get_product_name()
    # assert product_name == checkout_product_name
    CheckoutPage(browser).select_country(1)
    CheckoutPage(browser).select_first_delivery_method(1)
    CheckoutPage(browser).vipvip_button()
    # Переход на VipCoin
    VipFirstPage(browser).select_type_of_pay(1)
    VipSecondPage(browser).upload_keyfile(os.getcwd() + "/+500500000005user.keystore")
    VipSecondPage(browser).enter_password(password=password_for_key)
    VipSecondPage(browser).show_wallets()
    VipSecondPage(browser).confirm_withdrawal()
    VipSecondPage(browser).pay()
    time.sleep(5)
