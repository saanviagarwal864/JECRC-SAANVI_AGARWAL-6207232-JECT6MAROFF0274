from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
sleep(3)

##textboxes

first_name=driver.find_element(By.XPATH,'//input[@id="firstName"]')
first_name.clear()
first_name.send_keys('Saanvi')
sleep(1)

last_name=driver.find_element(By.XPATH,'//input[@id="lastName"]')
last_name.clear()
last_name.send_keys('Agarwal')
sleep(1)

email=driver.find_element(By.XPATH,'//input[@id="userEmail"]')
email.clear()
email.send_keys('abcd@gmail.com')
sleep(1)


mobile=driver.find_element(By.XPATH,'//input[@id="userNumber"]')
mobile.clear()
mobile.send_keys('1234567890')
sleep(1)


subjects=driver.find_element(By.ID,'subjectsInput')
subjects.clear()
subjects.send_keys('Maths')
subjects.send_keys(Keys.ENTER)
sleep(2)
subjects.send_keys('English')
subjects.send_keys(Keys.ENTER)
sleep(2)
subjects.send_keys('Chemistry')
subjects.send_keys(Keys.ENTER)


sleep(3)


current_address=driver.find_element(By.XPATH,'//textarea[@id="currentAddress"]')
current_address.clear()
current_address.send_keys('123 Main Street Nehru nagar jaipur')
sleep(2)


##radio button

gender=driver.find_element(By.XPATH,'//input[@id="gender-radio-2"]').click()
sleep(2)

##checkbox

hobby1=driver.find_element(By.XPATH,'//input[@id="hobbies-checkbox-1"]').click()
hobby2=driver.find_element(By.XPATH,'//input[@id="hobbies-checkbox-2"]').click()
sleep(2)


#upload file

picture=driver.find_element(By.ID,'uploadPicture')
picture.send_keys(r"C:\Users\agarw\Downloads\selenium-snapshot.png")
sleep(2)

#submit button

submit=driver.find_element(By.ID,"submit").click()
sleep(5)

driver.quit()