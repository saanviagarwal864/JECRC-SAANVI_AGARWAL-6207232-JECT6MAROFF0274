from selenium import webdriver
from os import name
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)
driver.get('https://www.testmuai.com/selenium-playground')
driver.maximize_window()
sleep(2)

##By ID
print('Locators using ID')
demo_form = driver.find_element(By.ID, 'demoForm')
print('demo_form found')
first_name = driver.find_element(By.ID, 'inputFirstName')
print('first_name found')
last_name = driver.find_element(By.ID, 'inputLastName')
print('last_name found')
email=driver.find_element(By.ID, 'inputEmail')
print('email found')
mobile = driver.find_element(By.ID, 'mobileid')
print('mobile id found')



## name
print('By name')
First_name= driver.find_element(By.NAME, 'first_name')
print('first_name found')
Last_name = driver.find_element(By.NAME, 'last_name')
print('last_name found')
Email = driver.find_element(By.NAME, 'email')
print('email found')
Mobile = driver.find_element(By.NAME, 'mobile_no')
print('mobile_no found')
message=driver.find_element(By.NAME, 'message')
print('message found')



## class
print('BY class name ')
nav_bar = driver.find_element(By.CLASS_NAME, 'chfw-container')
print('nav_bar found')
selenium_container = driver.find_element(By.CLASS_NAME, 'chfw-container__selenium')
print('selenium container found')
menu_link = driver.find_element(By.CLASS_NAME, 'chfw-menu-link')
print('menu_link found')
menu_item= driver.find_element(By.CLASS_NAME, 'chfw-menu-item')
print('menu_item found')
menu_description = driver.find_elements(By.CLASS_NAME, 'chfw-menu-description')
print('menu_description found')



