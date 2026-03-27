from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
sleep(3)

parent_window=driver.current_window_handle ##return you the particular window handle
print(driver.current_window_handle)
print(parent_window)


new_tab=driver.find_element(By.ID,"tabButton")
new_tab.click()
sleep(3)
driver.switch_to.window(driver.window_handles[-1])
print(driver.current_window_handle)
print((driver.find_element(By.XPATH,'//h1[@id="sampleHeading"]')).text)
assert 'sample page' in driver.find_element(By.XPATH,'//h1[@id="sampleHeading"]').text
print('Switched to new tab')
sleep(3)
driver.switch_to.window(parent_window)
sleep(3)


new_window=driver.find_element(By.ID,"windowButton")
new_window.click()
sleep(3)
driver.switch_to.window(driver.window_handles[-1]) ##recent window
print(driver.current_window_handle)
print(driver.find_element(By.XPATH,'//h1[@id="sampleHeading"]').text)
assert 'This is a sample page' == driver.find_element(By.XPATH,'//h1[@id="sampleHeading"]').text
print('Switched to new window')
sleep(3)
driver.switch_to.window(parent_window)
sleep(3)


new_window_message=driver.find_element(By.ID,"messageWindowButton")
new_window_message.click()
sleep(3)
driver.switch_to.window(driver.window_handles[-1]) ##recent window
print(driver.current_window_handle)
sleep(3)
driver.switch_to.window(parent_window)
sleep(3)
all_windows=driver.window_handles
print(len(all_windows))

driver.close()





