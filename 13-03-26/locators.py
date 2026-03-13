from os import name

from selenium import webdriver
from selenium.webdriver.common.by import By ##to take id
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

opts.add_argument('--headless') ##headless-->it makes sure that your browser runs in the atlas mode(in background)
# run scripts in background
driver = webdriver.Chrome(options=opts)


driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)

##id
# namee = driver.find_element(By.ID, 'name') ##find method return you the first element found
#and if not there then return no such element found exception
# phone_number=driver.find_element(By.ID, 'phone')
# print(namee) #<selenium.webdriver.remote.web_element.WebElement (session="230c99c6a995c1241ea8>
# print('name and phone number found')

##name
# nav_bar=driver.find_element(By.NAME, 'Navbar')
# print('nav bar found')

##class_name
# radio_button=driver.find_elements(By.CLASS_NAME, 'form-check-input')
# print('radio button found')
# print(radio_button)
# print(len(radio_button))
##if more than one radio button then returns list so we use find_elements and len(radio_button) will give 9

##Tag_name
# inp=driver.find_elements(By.TAG_NAME, 'input')
# print(len(inp))

##id class and name these have disadvantages as we can not find the unique elements


##finding using css this is the syntax of html right
# input[class="form-control"]
# input[type='radio']

##(attribute name and attribute value)
# animals=driver.find_elements(By.CSS_SELECTOR, 'select[id="animals"]')
# select tag ke andar ham id ka use karege to kind that particular id and we can find class also like this


##we use #for id and . for class
# animals=driver.find_elements(By.CSS_SELECTOR, '#animals')
# print('worked fine')

# form_control=driver.find_elements(By.CSS_SELECTOR, '.form-control')
# print('worked fine')



# <a href="http://testautomationpractice.blogspot.com/">Home</a>
#a[href*="testautomationpractice"] * is for partial(means any url that contains that string)
#a[href^="http://"] ^ is for starts with
#a[href$=".com"] $ is for ends with

#drawback of css selector
# we can not go back to parent we can only go down
# we can not find inner text

# div[class="widget-content"]
# div[class="widget-content"] a[href*="testautomationpractice.blogspot"]

### X path
#efficient and performs better
#traverse up  and down both
#find any element using inner text
#disadv-->it can be complex to write and understand and slower
# while css selectors  are easier to read
##we use relative xpath not absolute
##relative xpath-->// ex://input[@id='name']
##absolute xpath-->/  ex:html/body/div/input[@id='name']
##if we have more than one input tag then we use indexing
##ex-->(//input[@id='name'])[1]

enter_name=driver.find_element(By.XPATH, '//input[@placeholder="Enter Name"]')
enter_email=driver.find_element(By.XPATH, '//input[@placeholder="Enter EMail"]')
enter_phone_number=driver.find_element(By.XPATH, '//input[@placeholder="Enter Phone"]')
enter_form=driver.find_element(By.XPATH, '//div[@class="form-group"][5]')
script=driver.find_element(By.XPATH, '//script[@type="text/javascript"]')
blogId=driver.find_element(By.XPATH, '//meta[@itemprop="blogId"]')
form_element_url=driver.find_element(By.XPATH,'//*[@id="post-body-1307673142697428135"]/link[1]')
print('worked fine')

##inner text using xpath
# <a href="http://testautomationpractice.blogspot.com/">Home</a>
#//a[text()="Home"]
title=driver.find_element(By.XPATH,'//title[text()="Form Elements"]')
name_title=driver.find_element(By.XPATH,'//label[text()="Name:"]')
label=driver.find_element(By.XPATH,'//label[text()="Date Picker 3: (Select a Date Range)"]')

##if the content contains spaces then
France=driver.find_element(By.XPATH,'//option[contains(text(),"France")]')



##to find element of the table
#//td[text()="Animesh"]



