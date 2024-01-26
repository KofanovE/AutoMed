from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

"""
Program entering to olx account without true password and email
"""


options = webdriver.FirefoxOptions()

service = Service(executable_path = 'geckodriver')

driver = webdriver.Firefox(service=service)

driver.get("https://www.olx.ua/uk/")

i = 0
while i < 10:
    print(i+1)
    i = i +1
    time.sleep(1)
print()



time.sleep(1)
print('look for butoon registration')
print('')
but_reg = driver.find_element(By.CSS_SELECTOR, ".css-12l1k7f")

time.sleep(1)
print('click to butoon on frame')
print('')
but_reg.click()

i = 0
while i < 10:
    print(i+1)
    i = i +1
    time.sleep(1)
print()



time.sleep(1)
print('look for string for input email')
print('')
inp_email = driver.find_element(By.CSS_SELECTOR, '.css-2gs0sc')

time.sleep(1)
print('print email')
print('')
inp_email.send_keys("email")

time.sleep(1)
print('look for string for input pas')
print('')
inp_pas = driver.find_element(By.CSS_SELECTOR, '.css-ugcges')

time.sleep(1)
print('print pas')
print('')
inp_pas.send_keys("pas")

time.sleep(1)
print('look for butoon Enter')
print('')
but_ent = driver.find_element(By.CSS_SELECTOR, ".css-ypypxs")

time.sleep(1)
print('click to butoon enter')
print('')
but_ent.click()



