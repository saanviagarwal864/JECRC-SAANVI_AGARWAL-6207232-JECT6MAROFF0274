from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

opts.add_argument('--headless') ##headless-->it makes sure that your browser runs in the atlas mode(in background)
# run scripts in background
driver = webdriver.Chrome(options=opts)


driver.get('https://www.myntra.com')
sleep(3)
print('It is working fine')
