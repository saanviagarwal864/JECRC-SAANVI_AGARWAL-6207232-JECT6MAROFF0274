from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# sleep(5)
#
# ##dropdown will always be in select tag so will always import a class select to handle it
# #if not in select tag then click
# country_dropdown=driver.find_element(By.ID,"country") ##whole dropdown
# dropdown=Select(country_dropdown)
#
# ##3 ways to access the elements in dropdown
# dropdown.select_by_value('india')
# sleep(2)
# dropdown.select_by_visible_text("China")
# sleep(2)
# dropdown.select_by_index(3) ##in xpath indexing starts from 1 here it starts from 0
# sleep(2)

driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(5)
search=driver.find_element(By.XPATH,'//input[@placeholder="What are you looking for?"]')
search.send_keys("computer glasses",Keys.ENTER)
sleep(5)

bestseller_dropdown=driver.find_element(By.XPATH,'//select[@id="sortByDropdown"]')
sort=Select(bestseller_dropdown)
sleep(2)
# sort.select_by_index(4)
sort.select_by_value('saving')
sleep(3)

product1=driver.find_elements(By.XPATH,'//div[@class="sc-bf32d8a7-0 gOVKHN"]/descendant::p[@class="sc-23b7d3eb-2 dQrJBg"][1]')
print(product1[3].text)
print(len(product1))

product13=driver.find_element(By.XPATH,'(//div[@class="sc-bf32d8a7-0 gOVKHN"]/descendant::p[@class="sc-23b7d3eb-2 dQrJBg"])[13]')
print(product13.text)






driver.quit()





driver.quit()
