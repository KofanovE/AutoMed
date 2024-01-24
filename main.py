from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
import time

"""
driver_path = os.path.abspath('geckodriver') # абсолютный путь к драйверу браузера

print(driver_path)

options = webdriver.FirefoxOptions()

service = Service(executable_path = 'geckodriver')

driver = webdriver.Firefox(service=service) # создание экземпляра драйвера


driver.get('https://www.google.com/')

xpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]'
selector = '.FPdoLc > center:nth-child(1) > input:nth-child(2)'

print('1')
time.sleep(5)
print('2')

#button = driver.find_element_by_xpath(xpath)
button = driver.find_element_by_css_selector(selector)

#button.send_keys(Keys.ENTER)

button.click()
"""
driver_path = os.path.abspath('geckodriver') 


options = webdriver.FirefoxOptions()

service = Service(executable_path = 'geckodriver')

driver = webdriver.Firefox(service=service)

keyword = "geeksforgeeks"

driver.get("https://www.geeksforgeeks.org/")

print('1')
time.sleep(30)
print('2')

"""
element_gog_close = driver.find_element(By.CSS_SELECTOR, "svg.Bz112c:nth-child(2) > path:nth-child(1)")
print('3')
element_gog_close.click()



print('4')
"""
element = driver.find_element(By.CLASS_NAME, "darkMode-wrap")

print('3')

element.click()

print('4')

