from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utilities import constants


class SeleniumBase():

    def __init__(self, driver):
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def maximize(self):
        self._driver.maximize_window()

    def get_title(self):
        return self._driver.title

    def click(self, locator):
        self._driver.find_element_by_xpath(locator).click()

    def click_by_javascript(self, locator):
        js = self._driver.find_element_by_xpath(locator)
        self._driver.execute_script("arguments[0].click();", js)

    def wait_and_click(self, locator):
        element = WebDriverWait(self._driver, constants.WAIT_TIME_20_SEC).until(
            ec.visibility_of_element_located((By.XPATH, locator)))
        element.click()

    def wait_and_send_keys(self, locator, value):
        element = WebDriverWait(self._driver, constants.WAIT_TIME_20_SEC).until(
            ec.visibility_of_element_located((By.XPATH, locator)))
        element.send_keys(value)

    def is_element_visible(self, locator):
        element = WebDriverWait(self._driver, constants.WAIT_TIME_20_SEC).until(
            ec.visibility_of_element_located((By.XPATH, locator)))
        return element.is_displayed()

    def send_keys(self, locator, value):
        self._driver.find_element_by_xpath(locator).send_keys(value)

    def get_attribute(self, locator, name):
        element = WebDriverWait(self._driver, constants.WAIT_TIME_20_SEC).until(
            ec.presence_of_element_located((By.XPATH, locator)))
        return element.get_attribute(name)

    def close(self):
        self._driver.close()