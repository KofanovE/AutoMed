from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
import time


options = webdriver.FirefoxOptions()

service = Service(executable_path = 'geckodriver')

driver = webdriver.Firefox(service=service)

keyword = "geeksforgeeks"

driver.get("https://www.geeksforgeeks.org/")

time.sleep(30)

element = driver.find_element(By.CLASS_NAME, "darkMode-wrap")

element.click()



