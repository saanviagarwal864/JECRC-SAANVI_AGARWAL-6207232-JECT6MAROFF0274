# we can take screenshots using os ,screenshot will be stored where we are working so we want to
# make a separate folder for it to keep it clean, to access path related methods we use os
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#set path
folder=os.path.join(os.getcwd(), 'screenshots')
#it will join two things the directory you want and folder name
#os.getcwd we get current working directory path using this method

#create folder if not created
os.makedirs(folder,exist_ok=True)
#exists ok if directory present not show exception if not there then create

driver=webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(2)

##to take screenshot of whole page
#it will take folder and file name segregated by / as it will be saved as path
driver.save_screenshot(f'{folder}/full_page.png')
sleep(3)


##to take screenshot of particular element we find element first and then element.screenshot()
ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
#we can also use //img[contains(@alt,"Photo of a woman in a cherry")] as xpath
action=ActionChains(driver)
action.scroll_to_element(ele).perform()
sleep(2)

ele.screenshot(f'{folder}/element.png')
sleep(3)




