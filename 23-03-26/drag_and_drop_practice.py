from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
sleep(3)

##task 1: Drag and drop simple
# action=ActionChains(driver)
# origin_ele=driver.find_element(By.ID,'draggable')
# target_ele=driver.find_element(By.ID,'droppable')
#
# action.drag_and_drop(origin_ele,target_ele).perform()
# sleep(5)
#
# assert 'Dropped!' == target_ele.text,'did not drop'
# print('Drag and drop done')

##task 2:NESTED DRAG AND DROP using button and different areas

button=driver.find_element(By.ID,'droppableExample-tab-preventPropogation').click()
sleep(3)
action=ActionChains(driver)
origin_element=driver.find_element(By.ID,'dragBox')

outer_drop1=driver.find_element(By.XPATH,'//div[@id="notGreedyDropBox"]/descendant::p')
action.drag_and_drop(origin_element,outer_drop1).perform()
sleep(4)

inner_drop1=driver.find_element(By.XPATH,'//div[@id="notGreedyInnerDropBox"]/descendant::p')
action.drag_and_drop(origin_element,inner_drop1).perform()
sleep(4)

outer_drop2=driver.find_element(By.XPATH,'//div[@id="greedyDropBox"]/descendant::p')
action.drag_and_drop(origin_element,outer_drop2).perform()
sleep(4)

inner_drop2=driver.find_element(By.XPATH,'//div[@id="greedyDropBoxInner"]/descendant::p')
action.drag_and_drop(origin_element,inner_drop2).perform()
sleep(4)

driver.quit()

