from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.myntra.com')
driver.maximize_window()

# search=driver.find_element(By.XPATH, '//input[@placeholder="Search for products, brands and more"]')
# search.clear()
# search.send_keys('tops')
# print(search.get_attribute('value'))
# print(search.get_attribute('placeholder'))

##2 ways to click a button


##1st use keys.enter and it will search
# search=driver.find_element(By.XPATH, '//input[@placeholder="Search for products, brands and more"]')
# search.clear()
# search.send_keys('tops',Keys.ENTER)
# sleep(2)
# print(search.get_attribute('value'))
# print(search.get_attribute('placeholder'))
##this get attribiute will not work as it does not get time to process as it works very fast

##2nd make a search button and then use click() after we have done send keys on search
search=driver.find_element(By.XPATH, '//input[@placeholder="Search for products, brands and more"]')
search.clear()
search.send_keys('tops')
print(search.get_attribute('value'))
print(search.get_attribute('placeholder'))

search_button=driver.find_element(By.CLASS_NAME,'desktop-submit')
search_button.click()
sleep(2)
##if i write get attribute here after this it will not work because it gets cleared once we have searched so we need to find attribute again



driver.quit()



