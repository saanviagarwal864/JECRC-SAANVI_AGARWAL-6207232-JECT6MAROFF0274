# TAsk 3
# 1. navigate to amazon
# 2. search a product through send_keys
# BUT dont click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.amazon.in/")
driver.maximize_window()

wait=WebDriverWait(driver,15)

search=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="twotabsearchtextbox"]')))
search.send_keys("books")

product4=wait.until(EC.element_to_be_clickable((By.XPATH,'(//div[@class="s-suggestion-container"])[4]/descendant::div')))
product4.click()

sort_by=wait.until(EC.element_to_be_clickable((By.XPATH,'//span[@id="a-autoid-0-announce"]')))
sort_by.click()

newest=wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@id="s-result-sort-select_4"]')))
newest.click()

free_shipping=wait.until(EC.element_to_be_clickable((By.XPATH,'(//i[@class="a-icon a-icon-checkbox"])[1]')))
free_shipping.click()

product_name=wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@class="a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal"]/descendant::span')))


product_price=wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="sg-col-inner"])[5]/descendant::div[@data-cy="price-recipe"]/div/div/a/span')))
print(f'{product_name.text} = {product_price.text}')


driver.quit()
