from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)

# 1.Go to https://the-internet.herokuapp.com/login.
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()
sleep(2)

# 2.Locate the username field using XPath with Tag and name attribute.
username=driver.find_element(By.XPATH,'//input[@name="username"]')
print('username found')

# 3.Locate the password field using XPath with Tag and id attribute.
password=driver.find_element(By.XPATH,'//input[@id="password"]')
print('password found')

# 4.Locate the "Login" button using XPath with Tag and type attribute.
login=driver.find_element(By.XPATH,'//button[@type="submit"]')
print('login found')

# 5.Locate the "Elemental Selenium" link using its exact text with text().
Elemental_selenium=driver.find_element(By.XPATH,'//a[text()="Elemental Selenium"]')
print('elemental selenium found')

# 5.Locate the main heading "Login Page" using contains() with text.
login_page=driver.find_element(By.XPATH,'//h2[contains(text(),"Login")]')
print('login page found')
