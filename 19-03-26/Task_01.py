#1.got to abc site
#2. fetch all image links of svg banners (use for loop), use explicit waits instead of find element, use presence of element located
#3.pause the loading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get("https://abc.com/")
driver.maximize_window()

wait=WebDriverWait(driver,10)

##presence means present on dom and visibility means visible on ui
imagelinks=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="hero-items"]/descendant::picture/child::img')))
for image in imagelinks:
    print(image.get_attribute('src'))

# all_elements=list of all elements
driver.quit()




