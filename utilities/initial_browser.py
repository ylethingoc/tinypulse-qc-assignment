from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.base import SeleniumBase


def get_browser(browser):
    if browser.lower() == 'chrome':
        return SeleniumBase(webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options))
    elif browser.lower() == 'firefox':
        return SeleniumBase(webdriver.Firefox(executable_path=GeckoDriverManager().install()))
    elif browser.lower() == 'edge':
        return SeleniumBase(webdriver.Edge(EdgeChromiumDriverManager().install()))
    else:
        raise(Exception('{} browser not supported'.format(browser)))