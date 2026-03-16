from selenium import webdriver
from selenium.webdriver.common.by import By ##we can import .y keys and action changes from
from time import sleep


opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

##textbox
# name=driver.find_element(By.ID,'name')
# ##locator expression:'name' and by.id is locator type
# name.clear()
# ##claers what was already written in text bax so that it does not concatenate
# name.send_keys('Saanvi')
# ##input or show text in text field
# sleep(2)
# email=driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]')
# email.send_keys('email@yahoo.in')
# sleep(2)

# print(name.get_attribute('placeholder'))
# ##get what is written in textbox can be value or placeholder
# print(email.get_attribute('placeholder'))

# clear()-->clears what ever is there in text field

##radio button
# driver.find_element(By.ID,'male').click()
# sleep(2)
#
# ##checkbox
# driver.find_element(By.XPATH,'//label[text()="Monday"]/preceding-sibling::input').click()
# sleep(2)
#
# ##to get the inner text we use .text()
# # //input[@id="monday"]/following-sibling::label
# monday_checkbox=driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label')
# print(monday_checkbox.text)
# sleep(2)


##togglle between male and female using for loop
# for i in range(1,5):
#     driver.find_element(By.ID, 'male').click()
#     sleep(2)
#     driver.find_element(By.ID, 'female').click()
#     sleep(2)
#
# driver.quit()

##input using if-else:
# gender=input(f"Enter your gender: ")
# if gender=="Male":
#     driver.find_element(By.ID, 'male').click()
#     sleep(2)
# else:
#     driver.find_element(By.ID, 'female').click()
#     sleep(2)

##check all the checkbox one by one  from front then uncheck them from back
# days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
# for day in days:
#     driver.find_element(By.ID, day).click()
#     print(day.text)
#     sleep(2)
# for day in days[::-1]:
#     driver.find_element(By.ID, day).click()
#     print(day.text)
#     sleep(2)

days=driver.find_elements(By.XPATH,'//div[@class="form-group"][4]/descendant::div[@class="form-check form-check-inline"]/descendant::label')
for day in days:
    day.click()
    print(day.text)
    sleep(1)
for day in days[::-1]:
    day.click()
    # print(day.text)
    sleep(1)

driver.quit()




