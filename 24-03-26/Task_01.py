from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
driver.maximize_window()
sleep(3)

action = ActionChains(driver)

iframe = driver.find_element(By.ID, "result")
driver.switch_to.frame(iframe)


username=driver.find_element(By.XPATH,'//input[@id="username"]')
action.scroll_to_element(username).perform()
username.clear()
username.send_keys("amit")
sleep(3)
password=driver.find_element(By.ID,'password')
password.clear()
password.send_keys("abcd")
show_pwd=driver.find_element(By.ID,'showPsswd')
sleep(2)
action.click_and_hold(show_pwd).perform()
sleep(2)
action.release().perform()
sleep(2)

register_button=driver.find_element(By.CLASS_NAME,'submit')
register_button.click()
sleep(5)
driver.back()
sleep(2)

driver.switch_to.frame(iframe)
div=driver.find_element(By.XPATH,'//div[@class="container"]/descendant::h1')

assert "Registration"==div.text,print('did not find')
print('Found')

print('Done')
driver.quit()



