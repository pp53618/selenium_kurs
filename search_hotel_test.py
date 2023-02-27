import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("http://www.kurs-selenium.pl/demo/")
driver.maximize_window()
driver.find_element(By.XPATH, "//span[text()='Search by Hotel or City Name']").click()
driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element(By.XPATH, "//span[text()='Dubai']").click()
driver.find_element(By.NAME, "checkin").send_keys('24/02/2023')
driver.find_element(By.NAME, "checkout").send_keys('25/02/2023')

# Inne sposoby wyboru daty
#driver.find_element(By.NAME, "checkin").click()
#driver.find_element(By.XPATH, "//td[@class='day ' and text()='24']").click()
#elementy = driver.find_elements(By.XPATH, "//td[@class='day ' and text()='26']")
#for element in elementy:
#    if(element.is_displayed()):
#        element.click()
#        break

driver.find_element(By.ID, "travellersInput").click()
driver.find_element(By.ID, "adultInput").clear()
driver.find_element(By.ID, "adultInput").send_keys("4")
driver.find_element(By.ID, "childInput").clear()
driver.find_element(By.ID, "childInput").send_keys("4")
driver.find_element(By.XPATH, "//button[text()=' Search']").click()

#//h4[contains(@class='list_title')]//b
hotels = driver.find_elements(By.XPATH, "//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute('textContent') for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)

prices = driver.find_elements(By.XPATH, "//div[contains(@class, 'price_tab')]//b")
price_value = [price.get_attribute('textContent') for price in prices]
for cost in price_value:
    print("Cena to: " + cost)

assert hotel_names[0] == 'Jumeirah Beach Hotel'
assert hotel_names[1] == 'Oasis Beach Tower'
assert hotel_names[2] == 'Rose Rayhaan Rotana'
assert hotel_names[3] == 'Hyatt Regency Perth'

assert price_value[0] == '€20.24'
assert price_value[1] == '€46'
assert price_value[2] == '€73.60'
assert price_value[3] == '€138'

driver.quit()
time.sleep(5)