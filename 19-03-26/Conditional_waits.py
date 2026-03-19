##when we use selenium 4 things are running-->python,python for selenium,UI and dom structure
##they are running on different speeds
##if we use sleep then it stops the python execution so it is a very bad practice to use sleep so
#that is why we use waits to solve synchronization issues.
##how do you handle synchronization issues by explicit wait and writing better xpaths

##Conditional Waits
##2 types:
##implicit -->driver.implicitly_wait(5)
##wait for 5 sec to find element in DOM structure when found interact if not found exception
##global wait
##only applicable for all driver.find_elements
##if element not visible on screen then still work but will not interact so it is drawback of implicit that
#it only cares about whether the element is found or not

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get("https://abc.com/")
driver.maximize_window()

# driver.implicitly_wait(5)

# ele=driver.find_element(By.XPATH,'(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
# print(ele.get_attribute('src'))

##Explicit:
#waits for certain element until condition is satisfied
##import 2 things webdriver wait and expected condition(has all expected conditions if clickable visible etc)
# check multiple conditions
#confined to that particular element not global
#check if visible ,is enabled we check these conditions
##find element wait for condition to be satisfied  and give output

wait_obj=WebDriverWait(driver,10)

submit_button=wait_obj.until(EC.element_to_be_clickable((By.ID,'button'))) ##only wait until condition satisfied
submit_button.click()
##it will show timeout error exception if not found or clickable in both conditions so it is a drawback of explicit

##fluent wait
#-->part of explicit wait
##altering the polling frequency
##polling frequency but frequently or after how many milisec the element is found again and again in doms structure
##give poling frequency also in webdriverwait

wait_obj=WebDriverWait(driver,10,poll_frequency=200)

##we give tuples in all these methods
# EC.visibility_of_element_located()-->check visibility of element on UI
# EC.presence_of_element_located()-->if it is present in DOM, it will give True
# EC.invisibility_of_element_located()-->it will wait for that element to be invisible for eg pop ups, ads
# EC.alert_is_present()-->checks for alerts
# EC.presence_of_all_elements_located()-->will give list of elements present only in DOM structure not cares for UI
# EC.new_window_is_opened()-->it will wait for new tab to open
# EC.url_matches()-->to check url matches to whatever we passed to; uses regular expressions



driver.quit()





