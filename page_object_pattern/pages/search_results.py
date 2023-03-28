from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from page_object_pattern.locators.locators import SearchResultLocators
import logging
import allure

#class SearchResultsPage:

#    def __init__(self, driver):
#        self.driver = driver
#        self.hotel_names_xpath = "//h4[contains(@class,'list_title')]//b"
#        self.hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
#        self.hotel_names_xpath = SearchResultLocators.hotel_names_xpath
#        self.hotel_prices_xpath = SearchResultLocators.hotel_prices_xpath
        self.logger = logging.getLogger(__name__)

    @allure.step("Checking resuts travellers")
    def get_hotel_names(self):
        hotels = self.driver.find_elements(By.XPATH, SearchResultLocators.hotel_names_xpath)
        names = [hotel.get_attribute('textContent') for hotel in hotels]
        self.logger.info("Availabel hotel are: ")
        allure.attach(self.driver.get_screenshot_as_png(), name="results", attachment_type=AttachmentType.PNG)
        for name in names:
            self.logger.info(name)
        return names

    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, SearchResultLocators.hotel_prices_xpath)
        hotel_prices = [price.get_attribute('textContent') for price in prices]
        self.logger.info("Prices are: ")
        for cost in hotel_prices:
            self.logger.info(cost)
        return hotel_prices
