from selenium import webdriver
from time import sleep
driver=[webdriver.Chrome(),webdriver.Edge(),webdriver.Firefox()]
for browser in driver:
    browser.maximize_window()
    sleep(2)
    browser.quit()