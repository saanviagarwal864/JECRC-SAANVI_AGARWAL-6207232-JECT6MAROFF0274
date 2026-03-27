from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
sleep(2)

driver.find_element(By.XPATH, '//button[@id="alertButton"]').click()
sleep(2)
alert=driver.switch_to.alert
alert.accept()
sleep(2)

driver.find_element(By.XPATH, '//button[@id="timerAlertButton"]').click()
sleep(6)
alert=driver.switch_to.alert
alert.accept()
sleep(2)

alert3=driver.find_element(By.XPATH, '//button[@id="confirmButton"]')
alert3.click()
sleep(2)
alert=driver.switch_to.alert
alert.dismiss()
sleep(2)
result=driver.find_element(By.XPATH, '//span[@id="confirmResult"]')
assert "Cancel" in result.text,print("not canceled")
print("canceled")
driver.refresh()
driver.find_element(By.XPATH, '//button[@id="confirmButton"]').click()
sleep(2)
alert=driver.switch_to.alert
alert.accept()
sleep(2)
result=driver.find_element(By.XPATH, '//span[@id="confirmResult"]')
assert "Ok" in result.text,print("not confirmed")
print("confirmed")
sleep(2)

driver.find_element(By.XPATH,'//button[@id="promtButton"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.send_keys("querty")
alert.accept()
sleep(3)
confirmation=driver.find_element(By.XPATH,'//span[@id="promptResult"]')
assert "querty" in confirmation.text,print("cancelled")
print(f"confirmed : {confirmation.text}")
