from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        return self.driver.find_elements(by, selector)[index]

    def _click(self, selector, index=0):
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__element(selector, index)))
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        time.sleep(3)
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=10):
        time.sleep(3)
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index, link_text)))

    def _get_element_text(self, selector, index=0):
        time.sleep(3)
        return self.__element(selector, index).text

    def _wait_for_clickable(self, selector, link_text=None, index=0, wait=10):
        time.sleep(3)
        return WebDriverWait(self.driver, wait).until(
            EC.element_to_be_clickable(self.__element(selector, index, link_text)))

    def _upload_file(self, selector, file, index=0):
        time.sleep(3)
        element = self.__element(selector, index)
        element.send_keys(file)
