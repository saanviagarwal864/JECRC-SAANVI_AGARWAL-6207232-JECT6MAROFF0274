from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
sleep(3)

print(f'The title of the page is {driver.title}')
username=driver.find_element(By.XPATH,'//input[@placeholder="Username"]')
username.clear()
username.send_keys('Admin')
sleep(2)
password=driver.find_element(By.XPATH,'//input[@placeholder="Password"]')
password.send_keys('admin123')
sleep(2)
submit_button=driver.find_element(By.XPATH,'//button[@type="submit"]')
submit_button.click()
sleep(5)
print(f'The current url is {driver.current_url}')

if 'dashboard' in driver.current_url:
    print('Successful Login')

driver.quit()
