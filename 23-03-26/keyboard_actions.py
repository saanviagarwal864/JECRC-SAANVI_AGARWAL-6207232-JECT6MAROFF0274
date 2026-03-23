from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# driver=webdriver.Chrome()
# driver.get('https://supertails.com/')
# driver.maximize_window()
# sleep(3)

##Keyboard actions-->
# action = ActionChains(driver)
#
# ##PAGEUP AND PAGEDOWN only move 100pixels
#
# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(5)
# action.send_keys(Keys.PAGE_UP).perform()
# sleep(5)
#
# ##every keys_down has a keys_up
# action.key_down(Keys.CONTROL).send_keys('a').perform()#-->press control and send keys a to select all -->key press
# sleep(5)
# action.key_up(Keys.CONTROL).perform() ##key release
# sleep(5)
#

# driver = webdriver.Chrome()
# driver.get(r"C:\Users\agarw\OneDrive\Desktop\pycharm_project\Day-8_23-03-26\address_fields.html")
# driver.maximize_window()
# action = ActionChains(driver)
#
# ##copy and pasting for address fields
# present=driver.find_element(By.ID,'presentAddress')
# sleep(2)
# present.send_keys("Jawahar nagar, Jaipur, Rajasthan")
# permanent=driver.find_element(By.ID,'permanentAddress')
# sleep(2)

# present.click()
# action.key_down(Keys.CONTROL).send_keys("a").perform()
# action.key_up(Keys.CONTROL).perform()
# sleep(3)
# action.key_down(Keys.CONTROL).send_keys("c").perform()
# action.key_up(Keys.CONTROL).perform()
#
# permanent.click()
# sleep(2)
# action.key_down(Keys.CONTROL).send_keys("v").perform()
# action.key_up(Keys.CONTROL).perform()
# sleep(1)


driver = webdriver.Chrome()
driver.get(r"C:\Users\agarw\OneDrive\Desktop\pycharm_project\Day-8_23-03-26\index1.html")
driver.maximize_window()
action = ActionChains(driver)

driver.find_element(By.ID,'password').send_keys("saanvi")
sleep(3)
show_pwd=driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show_pwd).perform()
sleep(5)
action.release().perform()
sleep(3)
driver.quit()






