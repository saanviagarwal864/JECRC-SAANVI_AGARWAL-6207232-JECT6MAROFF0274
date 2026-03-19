from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com/john-jacobs-jj-e70118-c1-eyeglasses.html")
driver.maximize_window()
sleep(5)

eye=driver.find_element(By.ID,"lrd1")
# print(eye.text)

# assert 'EYEGLASSES' in eye.text,'did not find EYEGLASSES text'
##if true print success if false print error as did not find eyeglasses text

# assert 'Glasses' == eye.text,'did not find'
# print('success')

# assert is keyword in python
#it will check if the statement is true or not if true move further in execution if
# false then give error

##is enabled
check=driver.find_element(By.XPATH,'//h4[@class="sc-84016674-0 dbhRRC"]')
print(check.is_enabled())
sleep(2)
check.click()
sleep(2)
check2=driver.find_element(By.XPATH,'//div[@class="sc-a3b31f26-14 fDEfLM"]')
print(check2.is_enabled())


driver.quit()

