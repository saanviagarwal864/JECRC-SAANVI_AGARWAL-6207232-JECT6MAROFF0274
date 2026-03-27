##performing action on the new window by switching on it
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(3)

# parent_window=driver.current_window_handle ##return you the particular window handle
# print(driver.current_window_handle)
# print(parent_window)
#
# driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
# sleep(3)
# all_windows=driver.window_handles ##return list of all windows open
# ##switch to windows using indexing in list
# print(len(all_windows))
#
# driver.switch_to.window(all_windows[-1]) ##recent window
# print(driver.current_window_handle)
# # print(driver.find_element(By.CLASS_NAME,'example').text)
# assert 'New' in driver.find_element(By.CLASS_NAME,'example').text
# print('Switched to recent window')
# sleep(3)
#
# driver.switch_to.window(parent_window) ##move back to parent window
#
# assert 'Selenium' in driver.find_element(By.XPATH,'//a[text()="Elemental Selenium"]').text
# print('Back to parent window')

# even if we close the recent window by using driver.close() the control will not go back to
# the parent window we need to switch the control back to parent window

###opening a website in the new window
driver.switch_to.new_window('window')
driver.get("https://www.myntra.com/")
sleep(3)

##opening the website in the new tab
driver.switch_to.new_window('tab')
driver.get("https://www.cricbuzz.com/")
sleep(3)







