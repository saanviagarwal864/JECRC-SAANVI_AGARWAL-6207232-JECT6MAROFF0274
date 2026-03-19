from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(3)

checkboxes=driver.find_element(By.LINK_TEXT,"Checkboxes")
print('Checkboxes link found')
sleep(2)

Drag_and_Drop=driver.find_element(By.PARTIAL_LINK_TEXT,"Drag")
print('Drag and drop link found')

li_elements=driver.find_elements(By.TAG_NAME,"li")
print(f'Number of li elements found on page: {len(li_elements)}')

driver.get('https://the-internet.herokuapp.com/tables')
driver.maximize_window()
sleep(3)

Website=driver.find_element(By.XPATH,'(//td[text()="jdoe@hotmail.com"]/following-sibling::td[2])[1]')
print('Website found')

Delete_link=driver.find_element(By.XPATH,'(//td[text()="Bach"]/following-sibling::td[5]/descendant::a[2])[1]')
print('Delete link found')

Second_table=driver.find_element(By.XPATH,'//table[2]')
print('Second table found')

Table2_element=driver.find_element(By.XPATH,'//table[2]/descendant::tr[4]/descendant::td[4]')
print('Cell containing "$100.00" in table 2 found')


driver.quit()

