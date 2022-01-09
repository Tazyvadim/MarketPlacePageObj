from locators import HeaderLocators

class Header:

    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element_by_css_selector(HeaderLocators.card['css']).click()

    def go_to_wishlist(self):
        self.driver.find_element_by_css_selector(HeaderLocators.wish_list['css']).click()

    def go_to_mainpage(self):
        self.driver.find_element_by_css_selector(HeaderLocators.logo['css']).click()