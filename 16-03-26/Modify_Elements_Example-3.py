from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.flipkart.com")
driver.maximize_window()

search=driver.find_element(By.XPATH,'//form[@class="lilxh_ header-form-search"]/descendant::div[@class="Afujtw"]/descendant::input[@style="color:#3d3d3dff"]')
search.clear()
search.send_keys("mobiles")
sleep(2)
print(search.get_attribute('value'))

search_button=driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
sleep(5)
search_button.click()
sleep(2) ##used to stop python selenium will not stop

brand=driver.find_element(By.XPATH,'//div[@class="ybaCDx"]/following-sibling::div[text()="Apple"]')
sleep(2)
brand.click()
print(brand.text)
sleep(2)

image1=driver.find_element(By.XPATH,'//div[@class="lWX0_T"]/child::img[1]')
print(image1.get_attribute('src'))
sleep(2)

image3=driver.find_elements(By.XPATH,'//div[@class="lWX0_T"]/child::img')
print(image3[3].get_attribute('src'))
sleep(1)

driver.quit()


