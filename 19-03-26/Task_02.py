#NAVIGATE TO https://demo.automationtesting.in/Register.html
#FILL THE FORM
#CLICK ON SUBMIT BUTTON

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()

wait=WebDriverWait(driver,15)

username=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="username"]')))
username.send_keys("Saanvi Agarwal")

email=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="email"]')))
email.send_keys("abc@gmail.com")

telephone=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="tel"]')))
telephone.send_keys("+9112345678")

fax_no=driver.find_element(By.XPATH,'//input[@id="fax"]')
if fax_no.is_enabled():
    wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="fax"]')))
    fax_no.send_keys("345678")




upload_file=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@name="datafile"]')))
upload_file.send_keys(r"C:\Users\agarw\Downloads\selenium-snapshot.png")

gender=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@name="sgender"]')))
# gender.click()
select_gender=Select(gender)
select_gender.select_by_value("male")


experience=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@value="one"]')))
experience.click()

skill1=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@value="automationtesting"]')))
skill1.click()
skill2=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@value="java"]')))
skill2.click()

automation_tools=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@id="tools"]')))
tool=Select(automation_tools)
tool.select_by_value("selenium")

submit=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="submit"]')))
submit.click()

driver.quit()

