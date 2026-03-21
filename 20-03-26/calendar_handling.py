from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

##handling date by text
driver.find_element(By.ID,'datepicker').send_keys('04/30/2026',Keys.ENTER)

##handling date using calendar
month='May'
date='11'
year='2025'

driver.find_element(By.ID,'txtDate').click()
sleep(2)

select=Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]'))
select.select_by_visible_text(month)
select2=Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-year"]'))
select2.select_by_visible_text(year)
driver.find_element(By.XPATH,f'//a[text()={date}]/parent::td').click()

sleep(3)
driver.quit()
