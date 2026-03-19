from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(3)

beauty=driver.find_element(By.XPATH,'//a[@data-group="beauty"]')
print(beauty.text)

assert 'BEAUTY' == beauty.text,'did not find'
print('success')
driver.quit()