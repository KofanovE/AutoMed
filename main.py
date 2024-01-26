from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
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
print()


"""
#
# Close all windows, without parent's
#

parent = driver.current_window_handle
uselessWindows = driver.window_handles
print("Parent:", parent)
for winId in uselessWindows:
    print(winId)
    if winId != parent:
        driver.switch_to.window(windId)
        driver.close()
"""


"""
#
# Work with contener or form
#

print('look for a form')
print('')
# Find a form contener
iframe = driver.find_element(By.CSS_SELECTOR, '#credential_picker_container > iframe:nth-child(1)')


print('connect to form')
print('')
# Connect to contener
driver.switch_to.frame(iframe)


time.sleep(1)
print('look for butoon on frame')
print('')
# Find a button in form
but_close = driver.find_element(By.ID, "close")

time.sleep(1)
print('click to butoon on frame')
print('')
# Close form by button close
but_close.click()


time.sleep(1)
print('switch to main frame')
print('')
# Return to main form
driver.switch_to.default_content()
"""



#
# Working with child_menu
#

time.sleep(1)
print('look for select menu')
print('')
# Find an item of mainmenu 
select = driver.find_element(By.CSS_SELECTOR, 'li.header-main__list-item:nth-child(3)')

time.sleep(1)
print('select a parent punct')
print('')
# Move a cursor to item of mainmenu
ActionChains(driver).move_to_element(select).perform()


"""
#
# Writing text of 2 item of menu
#

time.sleep(1)
print('look for  menu')
print('')
menu = driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul[1]/li[3]/ul/li[2]')

print(menu.text)
print()
"""



time.sleep(3)
print('look for child menu')
print('')
# Find an item in 1_child_menu
select_2 = select.find_element(By.CSS_SELECTOR, 'li.header-main__list-item:nth-child(3) > ul:nth-child(3) > li:nth-child(6)')


time.sleep(3)
print('select a child menu')
print('')
# Move a cursor on item in 1_child_menu
ActionChains(driver).move_to_element(select_2).perform()


time.sleep(3)
print('look for child punct')
print('')
# Find an item in 2_child_menu
select_3 = select_2.find_element(By.CSS_SELECTOR, 'li.selected:nth-child(6) > ul:nth-child(3) > li:nth-child(1)')


time.sleep(3)
print('select a child punct')
print('')
# Click on item in 2_child_menu
select_3.click()




"""
#
# Press on button
#

time.sleep(1)
print('look for darkMode button')
print('')


element = driver.find_element(By.CLASS_NAME, "darkMode-wrap")

time.sleep(1)
print('click to darkMode button')
print('')

element.click()
"""




"""
#
# Input and clear text in line
#

time.sleep(1)
print('look for string for input text')
print('')

element_text = driver.find_element(By.CSS_SELECTOR, '.ant-input')

time.sleep(1)
print('print text 1')
print('')

element_text.send_keys("The first text...")

time.sleep(1)
print('delete text 1')
print('')

element_text.clear()

time.sleep(1)
print('print text 2')
print('')

element_text.send_keys("The second text!")

time.sleep(1)
print('delete text 2')
print('')

element_text.clear()
"""

