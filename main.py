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


i = 0
while i < 10:
    print(i+1)
    i = i +1
    time.sleep(1)

"""
parent = driver.current_window_handle
uselessWindows = driver.window_handles
print("Parent:", parent)
for winId in uselessWindows:
    print(winId)
    if winId != parent:
        driver.switch_to.window(windId)
        driver.close()
"""
print('look for a form')
print('')
iframe = driver.find_element(By.CSS_SELECTOR, '#credential_picker_container > iframe:nth-child(1)')


print('connect to form')
print('')
driver.switch_to.frame(iframe)



time.sleep(1)
print('look for butoon on frame')
print('')
but_close = driver.find_element(By.ID, "close")

time.sleep(1)
print('click to butoon on frame')
print('')
but_close.click()


time.sleep(1)
print('switch to main frame')
print('')
driver.switch_to.default_content()



time.sleep(1)
print('look for darkMode button')
print('')


element = driver.find_element(By.CLASS_NAME, "darkMode-wrap")

time.sleep(1)
print('click to darkMode button')
print('')

element.click()

time.sleep(1)
print('look for string for input text')
print('')

element_text = driver.find_element(By.CSS_SELECTOR, '.ant-input')

time.sleep(1)
print('print text 1')
print('')

element_text.send_keys("The first text...")

time.sleep(3)
print('delete text 1')
print('')

element_text.clear()

time.sleep(3)
print('print text 2')
print('')

element_text.send_keys("The second text!")


