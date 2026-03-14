from selenium import webdriver
from time import sleep

##when opening different urls we navigate to the last url
driver = webdriver.Chrome()
driver.get('https://www.amazon.com')
sleep(2)
driver.get('https://www.myntra.com/')
sleep(2)
driver.get('https://cricbuzz.com')
sleep(2)

