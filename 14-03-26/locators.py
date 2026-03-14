##ex: //input[@id="username"]/ancestor::div[@class=""]

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
# driver.get('https://www.amazon.com/')
# sleep(2)

##Finding all using ancestor:
# all_nav=driver.find_elements(By.XPATH,'//span[text()="All"]/ancestor::div[@id="nav-main"]')
# print('all_nav found using ancestor')
# figure_anc=driver.find_elements(By.XPATH,'//span[text()="Figurines, vases & more"]/ancestor::div[@id="gw-layout"]')
# print('figure found using ancestor')
#
# ##all using descendant:
# all_des=driver.find_elements(By.XPATH,'//div[@id="nav-main"]/descendant::span[text()="All"]')
# figures_des=driver.find_elements(By.XPATH,'//div[@id="gw-layout"]/descendant::span[text()="Figurines, vases & more"]')
# print('figures found using descendent')

##using preceding-sibling and following-sibling
##a[text()="Fresh"]/ancestor::li/following-sibling::li[1]
##a[text()="Fresh"]/ancestor::li/preceding-sibling::li[1]
# fresh_sibling=

driver.get('https://testautomationpractice.blogspot.com/')
##Link text and partial link text
#-->use when there is link attached to tag and with link there should be an inner text present in it
driver.find_element(By.LINK_TEXT,"Udemy Courses")
print('Udemy Courses using link text')
driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")
print('Udemy Courses using partial link text')

##using learn java find 500
price=driver.find_element(By.XPATH,'//td[text()="Learn Java"]/following-sibling::td[3]')
print('price found')

##using amod find selenium
amod=driver.find_element(By.XPATH,'//td[text()="Amod"]/ancestor::tbody/descendant::tr[2]/child::td[3]')
print('amod to selenium')

##from price=300 to bookname use find_elements
booklist_300=driver.find_elements(By.XPATH,'//td[text()="300"]/preceding-sibling::td[3]')
print(len(booklist_300))

##all browser from table
browsers=driver.find_elements(By.XPATH,'//tbody[@id="rows"]/child::tr/descendant::td[1]')
print(len(browsers))
for i in browsers:
    print(i.text)



