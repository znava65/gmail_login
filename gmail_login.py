# Author: Eduard Znava

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import sys

args = sys.argv
if len(args) < 3:
    print('You need to provide email/phone number and password in arguments')
    exit(-1)

identifier = args[1]
password = args[2]

print('Opening the browser...')
driver = uc.Chrome(use_subprocess=True)
driver.implicitly_wait(7)
driver.get('https://www.gmail.com')

print('Trying to login...')
driver.find_element(by=By.ID, value='identifierId').send_keys(identifier)
driver.find_element(by=By.ID, value='identifierNext').click()

try:
    driver.find_element(by=By.XPATH, value='//div[@id ="password"]/div[1]/div/div[1]/input').send_keys(password)
except NoSuchElementException:
    print('Invalid email/phone number')
    exit(-1)

driver.find_element(by=By.ID, value='passwordNext').click()

time.sleep(10)
if driver.current_url.startswith('https://accounts.google.com/signin'):
    print('Invalid password')
    exit(-1)
else:
    print('Login successful')

time.sleep(5)
