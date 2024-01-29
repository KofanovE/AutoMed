from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from cred import email, key
from patients import first_name, second_name, birthday_date
import os
import time


options = webdriver.FirefoxOptions()

service = Service(executable_path = 'geckodriver')

driver = webdriver.Firefox(service=service)

driver.get("https://id.helsi.pro/")

i = 0
while i < 5:
    print(i+1)
    i = i +1
    time.sleep(1)
print()

time.sleep(1)
print('look for email input line')
print()
email_line = driver.find_element(By.CSS_SELECTOR, '#email')

time.sleep(1)
print('send email')
print()
email_line.send_keys(email)

time.sleep(1)
print('look for key input line')
print()
cred_line = driver.find_element(By.CSS_SELECTOR, '#usercreds')

time.sleep(1)
print('send key')
print()
cred_line.send_keys(key)

time.sleep(1)
print('look for key button enter')
print()
enter_btn = driver.find_element(By.CSS_SELECTOR, '.btn')

time.sleep(1)
print('press enter')
print()
enter_btn.click()

i = 0
while i < 20:
    print(i+1)
    i = i +1
    time.sleep(1)
print()

time.sleep(1)
print('look for key button patient')
print()
patient_btn = driver.find_element(By.CSS_SELECTOR, 'div.col-xs-12:nth-child(6) > a:nth-child(1) > div:nth-child(1)')

time.sleep(1)
print('press button patient')
print()
patient_btn.click()

"""
.has-error > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)
.has-error > div:nth-child(2) > div:nth-child(1)
/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div[2]/div/input
"""

time.sleep(3)
print('look for line input second name')
print()
second_name_line = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div[2]/div/input')

time.sleep(1)
print('send second name')
print()
second_name_line.send_keys(second_name)

time.sleep(3)
print('look for line input first name')
print()
first_name_line = driver.find_element(By.CSS_SELECTOR, 'div.form-group:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)')

time.sleep(1)
print('send first name')
print()
first_name_line.send_keys(first_name)

time.sleep(3)
print('look for key line input birthday date')
print()
birthday_line = driver.find_element(By.CSS_SELECTOR, '.input__maskedDate')

time.sleep(1)
print('send birthday date')
print()
birthday_line.send_keys(birthday_date)




