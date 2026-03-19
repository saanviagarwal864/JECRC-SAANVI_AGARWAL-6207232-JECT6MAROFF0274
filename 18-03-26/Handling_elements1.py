from selenium import webdriver
from selenium.webdriver.common.by import By ##we can import .y keys and action changes from
from time import sleep


opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

##3 methods that give boolean output
# male.is_displayed()->if displayed or not ( visible on screen or not)
# male.is_enabled()-> for button if it is enabled or not only for button
# male.is_selected()->checkbox or dropdown is selected or not

male=driver.find_element(By.ID,'male')
male.click()
print(male.is_displayed())
print(male.is_enabled())

check=driver.find_element(By.XPATH,'//label[text()="Monday"]/preceding-sibling::input')
check.click()
print(check.is_selected())

monday_checkbox=driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label')
print(monday_checkbox.text)

driver.quit()


