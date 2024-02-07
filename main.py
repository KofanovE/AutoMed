import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
from cred import email, key
from doctors import full_doctors_list
import os
import time

current_date = datetime.now()
dead_time = current_date - timedelta(20)


# read DF Complete episodes
try:
    df_complete_episodes = pd.read_excel("Complete_Episodes.xlsx")
except FileNotFoundError:
    data = {'id': [],
            'Ready': [],
            'Status' : [],
            'Creation' : [],
            'Surname': [],
            'Name': [],
            'Birthday': [],
            'Прудченко О. В.': [],
            'Бабенко О. І.': [],
            'Білай-Рижова Ю. С.': [],
            'Трегуб Е. В.': [],
            'Бальченко І. С.': [],
            'Андрєєв Ю. Ф.': [],
            'Тушинський К. С.': [],
            'episode': []
            }
    df_complete_episodes = pd.DataFrame(data)

#df_complete_episodes.set_index('id', inplace=True)
print(df_complete_episodes)
print()

# read DF Patients
try:
    df_patients = pd.read_excel("Patients.xlsx")
except FileNotFoundError:
    df_patients = pd.DataFrame()



options = webdriver.FirefoxOptions()

service = Service(executable_path = 'geckodriver')

driver = webdriver.Firefox(service=service)

driver.get("https://id.helsi.pro/")



""" Authorization """

print('look for email input line and send email')
print()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#email'))).send_keys(email)

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

time.sleep(2)

print('look for button patient and press it')
print()
btn = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.col-xs-12:nth-child(6) > a:nth-child(1) > div:nth-child(1)')))
time.sleep(2)
btn.click()






for index, row in df_patients.iterrows():
    second_name = row["Surname"]
    first_name = row["Name"]
    birthday_date = row["Birthday"]

    print("#1", second_name, first_name, birthday_date)
    



    

    """ Cicle working with episodes """


    print('look for input second name and send it')
    print()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div[2]/div/input'))).send_keys(second_name)

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
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.margin-left-offset-20 > button:nth-child(1)'))).click()



    print('look for button operation with patient')
    print()
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-text-lg > span:nth-child(1) > svg:nth-child(1)'))).click()
    except TimeoutException:
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.active > a:nth-child(1) > span:nth-child(1) > svg:nth-child(1)'))).click()
        print("Uncorrect data")
        # write data to specil file
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div[2]/div/input'))).clear()
        driver.find_element(By.CSS_SELECTOR, 'div.form-group:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)').clear()
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/form/div[1]/div[3]/div/div[2]/div/div/input').clear()
        continue

    
    print('look for button episode')
    print()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.ant-dropdown-menu-item:nth-child(4) > span:nth-child(1) > a:nth-child(1)'))).click()

    print('look for all episodes')
    print()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-table-content')))



    
    

    time.sleep(3)
    episodes = driver.find_element(By.CSS_SELECTOR, '.ant-table-content')
    rows_episodes = episodes.find_elements(By.TAG_NAME, 'tr')

    
    

    exit_loop = False

    # Check all episodes of current pacient
    for row in rows_episodes:
        if exit_loop:
                print("!!! 4")
                break
        cells = row.find_elements(By.TAG_NAME, 'td')
        i = 0
        for cell in cells:
            #print(i, '. ', cell.text)
            
            if i == 1:
                print('#', cell.text)
                print()
                if "Z02.3" in cell.text:
                    selected_episode = cell
                    doctors_list = full_doctors_list.copy()
                    selected_episode.click()
                    print('look for all reception')
                    print()
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ant-table-tbody')))
                    time.sleep(3)

                    status_episode = driver.find_element(By.CSS_SELECTOR, 'div.col-md-12:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
                    print('status: ', status_episode.text)
                    print()

                    date = driver.find_element(By.CSS_SELECTOR, 'div.col-md-12:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
                    create_episode = datetime.strptime(date.text[:10], '%d.%m.%Y')
                    print('create: ', create_episode)
                    print()


                    num_episode = driver.find_element(By.CSS_SELECTOR, '.col-md-4 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
                    print('num_episode: ', num_episode.text)
                    print()
                    

                    
        
                    receptions = driver.find_element(By.CSS_SELECTOR, '.ant-table-tbody')
                    rows_receptions = receptions.find_elements(By.TAG_NAME, 'tr')
                    # Check all punkts of current episode
                    for row in rows_receptions:
                        cells_episode = row.find_elements(By.TAG_NAME, 'td')
                        j = 0
                        for cell_episode in cells_episode:
                            #print('#', cell_episode.text)
                            if j == 5:
                                #print('Here!')
                                if cell_episode.text in doctors_list:
                                    
                                    doctors_list.remove(cell_episode.text)                     
                            j = j + 1
                    if status_episode.text == 'Завершений':
                        ready_episode = "Closed"
                    elif create_episode < dead_time:
                        ready_episode = "Delay"
                    elif not doctors_list:
                        ready_episode = "Ready"
                    else:
                        ready_episode = "Not ready"
                    
                    if not df_complete_episodes['episode'].str.contains(num_episode.text).any():
                        series_index = len(df_complete_episodes) + 1
                    else:
                        series_index = df_complete_episodes.loc[df_complete_episodes['episode'] == num_episode.text].index[0]+1
                    
                    
                    
                    data_episode = {'id': series_index,
                                    'Ready': ready_episode,
                                    'Status' : status_episode.text,
                                    'Creation' : date.text[:10],
                                    'Surname': second_name,
                                    'Name': first_name,
                                    'Birthday': birthday_date,
                                    'Прудченко О. В.': True,
                                    'Бабенко О. І.': True,
                                    'Білай-Рижова Ю. С.': True,
                                    'Трегуб Е. В.': True,
                                    'Бальченко І. С.': True,
                                    'Андрєєв Ю. Ф.': True,
                                    'Тушинський К. С.': True,
                                    'episode': num_episode.text,
                                    }

                    
                    new_episode = pd.Series(data_episode)
                    print(new_episode)
              
                                                   

                    
                    if doctors_list:
                        for doctor in doctors_list:
                            new_episode[doctor] = False


                    
                    
                    if not df_complete_episodes['episode'].str.contains(num_episode.text).any():
                        print('!!! 1')
                        df_complete_episodes = pd.concat([df_complete_episodes, new_episode.to_frame().T], ignore_index=True)
                    else:
                        row_index = df_complete_episodes.loc[df_complete_episodes['episode'] == num_episode.text].index[0]
                        for key, value in new_episode.items():
                            df_complete_episodes.at[row_index, key] = value
                        print('!!! 2')

                    exit_loop = True
                    print("!!! 3")
                    break
                                    
                    
                else:
                    # Not episode z02.3                   
                    break
            
            
            i = i + 1

    
             
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.active > a:nth-child(1) > span:nth-child(1) > svg:nth-child(1)'))).click()

    if index == len(df_patients) - 1:
        df_complete_episodes.to_excel("Complete_Episodes.xlsx", index=False)


"""


            elif i == 3:
                specified_date = datetime.strptime(cell.text[:10], '%d.%m.%Y')
                print('#', specified_date)
                if specified_date > dead_time:
                    # If time is ok, and it's z02.3




            if not doctors_list:
                        print('!!! Episode closed !!!')
                        print()
                        # Chek the carrent pacient in episode list
                        coincidence = df_complete_episodes[(df_complete_episodes['Surname'] == second_name) & (df_complete_episodes['Name'] == first_name) & (df_complete_episodes['Birthday'] == birthday_date)]
                        if coincidence.empty:
                            data = {'Surname': second_name, 'Name': first_name, 'Birthday': birthday_date}
                            df_complete_episodes = df_complete_episodes.append(data, ignore_index=True)
                            df.to_excel("Complete_Episodes.xlsx", index=False)
                        
                        else:
                            print("Episode was written")
                            print("___________________")
                            print()
            
                    else:
                        print('Remaining doctors: ', doctors_list)
                    break

"""


