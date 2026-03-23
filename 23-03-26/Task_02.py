from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(3)

action = ActionChains(driver)

women=driver.find_element(By.XPATH,'(//div[@class="desktop-navLink"]/descendant::a[@class="desktop-main"])[2]')
action.move_to_element(women).perform()
sleep(2)

heels=driver.find_element(By.XPATH,'//li[@data-reactid="259"]')
heels.click()
sleep(3)

row_five=driver.find_element(By.XPATH,'//li[@id="34837855"]')
action.scroll_to_element(row_five).perform()
sleep(5)

print('Done')

driver.quit()



