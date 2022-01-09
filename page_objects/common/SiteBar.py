from locators import SiteBarLocators

class SiteBar:

    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element_by_css_selector(SiteBarLocators.go_to_card['css']).click()

    def go_to_checkout(self):
        self.driver.find_element_by_css_selector(SiteBarLocators.go_to_checkout['css']).click()