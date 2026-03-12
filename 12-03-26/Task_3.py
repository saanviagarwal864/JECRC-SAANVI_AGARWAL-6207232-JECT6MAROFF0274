from selenium import webdriver
from time import sleep

drivers=[webdriver.Chrome(),webdriver.Firefox(),webdriver.Edge()]
for driver in drivers:
    driver.get("https://supertails.com")
    sleep(2)
    print('Title:',driver.title)
    print('Browser:',driver.current_url)
    print('Browser name:',driver.name)
    driver.close()
