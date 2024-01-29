from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from cred import email, key
from patients import first_name, second_name, birthday_date
import os
import time


options = webdriver.FirefoxOptions()

service = Service(executable_path = 'geckodriver')

driver = webdriver.Firefox(service=service)

driver.get("https://id.helsi.pro/")

print('look for email input line and send email')
print()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#email'))).send_keys(email)

print('look for key input line')
print()
cred_line = driver.find_element(By.CSS_SELECTOR, '#usercreds')

print('send key')
print()
cred_line.send_keys(key)

print('look for key button enter')
print()
enter_btn = driver.find_element(By.CSS_SELECTOR, '.btn')

print('press enter')
print()
enter_btn.click()

print('look for button patient and press it')
print()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.col-xs-12:nth-child(6) > a:nth-child(1) > div:nth-child(1)'))).click()

print('look for email input second name and send it')
print()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div[2]/div/input'))).send_keys(second_name)

print('look for line input first name')
print()
first_name_line = driver.find_element(By.CSS_SELECTOR, 'div.form-group:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)')

print('send first name')
print()
first_name_line.send_keys(first_name)

print('look for key line input birthday date')
print()
birthday_line = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/form/div[1]/div[3]/div/div[2]/div/div/input')

print('click on line input birthday')
print()
birthday_line.click()

print('send birthday date')
print()
birthday_line.send_keys(birthday_date)

print('look for button find a patient and press it')
print()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.margin-left-offset-20 > button:nth-child(1)'))).click()

print('look for button operation with patient')
print()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-text-lg > span:nth-child(1) > svg:nth-child(1)'))).click()

print('look for button episode')
print()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.ant-dropdown-menu-item:nth-child(4) > span:nth-child(1) > a:nth-child(1)'))).click()






