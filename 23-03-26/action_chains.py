##IT IS A CLASS THAT contains methods for keyboard and mouse actions
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#Drag and drop
# driver=webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# sleep(3)
#
# action=ActionChains(driver)
#
# origin_ele=driver.find_element(By.ID,'column-a')
# target_ele=driver.find_element(By.ID,'column-b')
#
# action.drag_and_drop(origin_ele,target_ele).perform()
# ##.perform() so that we can see that action being performed if we do not use then the action chains will not perform
# sleep(5)


driver=webdriver.Chrome()
driver.get('https://supertails.com/')
driver.maximize_window()
##Mouse Hover
# action=ActionChains(driver)
#
# dogg=driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])[1]')
# sleep(3)
# action.move_to_element(dogg).perform()
#
# # sleep(3)

#SCROLL
# action=ActionChains(driver)
#
# cat=driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
# action.scroll_to_element(cat).perform()
# sleep(3)

##Scroll to : it will scroll to the particular pixel or element
##Scroll by : it will scroll from the current pixel to that particular pixel relative to the current give two values x axis and y axis
##if we want to scroll up then negative values and if scroll down then positive values

# action.scroll_by_amount(0,-1500).perform()
# sleep(3)

#from:
# action.scroll_from_origin((0,0),0,1000).perform()
# sleep(3)

##CLICK
# left click-->normal click
# right click-->context click
# double click














