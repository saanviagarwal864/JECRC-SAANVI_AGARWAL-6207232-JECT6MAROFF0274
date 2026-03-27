from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
sleep(3)


##3 types of alerts:
#Simple alert / JavaScript alert-->only accept
# driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
# sleep(3)
# alert=driver.switch_to.alert
# alert.accept()
# sleep(3)

#Confirmation alert-->has two options accept and dismiss
# driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
# sleep(3)
# alert=driver.switch_to.alert
# # alert.accept() -->to accept
# alert.dismiss() #-->to cancel
# sleep(3)


#Prompt alert-->has a text field->accept, dismiss and send keys
# driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
# sleep(3)
# alert=driver.switch_to.alert
# alert.send_keys("querty")
# # alert.accept()
# alert.dismiss()
# sleep(3)

#switching to alert using waits
wait=WebDriverWait(driver,10)
driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
alert=wait.until(EC.alert_is_present())
# -->alert is present it will wait for that alert to pop up and switch to it
sleep(3)
alert.accept()
sleep(3)


