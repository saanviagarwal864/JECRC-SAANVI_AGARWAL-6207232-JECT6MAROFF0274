from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/radio-button')
driver.maximize_window()
sleep(3)

print(f'The title of the page is {driver.title}')

yes_button=driver.find_element(By.XPATH,'//input[@id="yesRadio"]')
yes_button.click()
sleep(2)
result_message=driver.find_element(By.XPATH,'//p[@class="mt-3"]')
print(result_message.text)
sleep(2)
print(result_message.get_attribute('class'))
print(yes_button.get_attribute('id'))
print(f'The current url is {driver.current_url}')
driver.quit()



