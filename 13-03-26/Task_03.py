from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
opts.add_argument('headless')
driver = webdriver.Chrome(options=opts)

# 1. Navigate to https://www.amazon.in/
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)

# 2. Locate the main search bar using its ID with a CSS Selector.
search_bar=driver.find_element(By.CSS_SELECTOR,'input[id="twotabsearchtextbox"]')
search_bar1=driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
print('search bar found')

# 3. Locate the Amazon logo (usually an <a> tag with an ID like nav-logo sprites) using a CSS Selector.
logo=driver.find_element(By.CSS_SELECTOR,'a[id="nav-logo-sprites"]')
logo1=driver.find_element(By.CSS_SELECTOR,'#nav-logo-sprites')
print('logo found')

# 4. Locate the "Cart" link/icon (often has an ID like nav-cart) using a CSS Selector.
cart_icon=driver.find_element(By.CSS_SELECTOR,'span[class="nav-cart-icon nav-sprite"]')
cart_icon1=driver.find_element(By.CSS_SELECTOR,'.nav-cart-icon.nav-sprite')
print('cart icon found')

# 5. Locate the "Sign in" link in the navigation bar (It might be inside a div with an ID like nav-tools. Use descendant way (space)).
sign_in=driver.find_element(By.CSS_SELECTOR,'div[id="nav-tools"] div[id="nav-link-accountList"] span[id="nav-link-accountList-nav-line-1"]')
sign_in1=driver.find_element(By.CSS_SELECTOR,'#nav-tools #nav-link-accountList .nav-line-1-container #nav-link-accountList-nav-line-1')
print('sign-in link found')

# 6. Locate all the main category links in the navigation bar under "All"(e.g."Best Sellers", "Mobiles", "Today's Deals").
# Inspect their common parent and use descendant way and to find all the <a> tags within it.Use find_elements and print the count.
all_categories=driver.find_elements(By.CSS_SELECTOR,'div[id="nav-xshop"] a')
all_categories1=driver.find_elements(By.CSS_SELECTOR,'#nav-xshop a')
print('all categories found')
print(len(all_categories1))