##sometimes the ui is not scrolling so we use javascript executor
##it works from the backend to scroll and to click
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(3)

#for all elements
##camel case for the words in js
#scrollheight->scrolls till the footer
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(3)
#
# ##scroll to origin of the page
driver.execute_script("window.scrollTo(0,0);")
sleep(3)
#in scroll to we can not give negative values because it goes to particular element it can not be negative value
##if we give negative value then it will consider it as 0 only

#using scroll by
driver.execute_script("window.scrollBy(0,500);")##scrolling down 500px from origin
sleep(3)
driver.execute_script("window.scrollBy(0,-200);")##scrolling up 200px from 500px
sleep(3)

#scrolling to particular element
ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
driver.execute_script("arguments[0].scrollIntoView();",ele)
sleep(3)

##clicking on the element
join_ele=driver.find_element(By.XPATH,'(//div[@class="lIkAnG eMU5i5 o5UlW_ hL1e7w"])[2]')
driver.execute_script('arguments[0].click();',join_ele)
sleep(3)





