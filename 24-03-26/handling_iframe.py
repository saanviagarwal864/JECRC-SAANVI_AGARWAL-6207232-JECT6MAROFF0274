#nested html
#iframe tag is used in html inside html tag
#so we switch to iframe to perform any action in iframe as it start the cursor is at the website page

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(3)

# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("123")
# this will not work as this text field is inside the iframe tag so show no such element found

#Single iframe
# iframe=driver.find_element(By.ID,'singleframe') ##finding the iframe
# driver.switch_to.frame(iframe)
# sleep(3)
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("123") ##finding text box inside iframe
# sleep(3)

#Nested iframes
driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()
sleep(3)

nested_iframe1=driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe1)
sleep(3)
nested_iframe2=driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(nested_iframe2)
sleep(3)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("123")
sleep(3)

##swith to parent iframe
driver.switch_to.parent_frame()
##switch to default page
driver.switch_to.parent_frame()

##directly move to default page
driver.switch_to.default_content()
sleep(3)





