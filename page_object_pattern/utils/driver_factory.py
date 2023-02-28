from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            return webdriver.Firefox(service=Service(executable_path=GeckoDriverManager.install()), options=options)
        raise Exception('Provide valid driver name')