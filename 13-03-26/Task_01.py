from selenium import webdriver
from selenium.webdriver.common.by import By ##to take id
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

# opts.add_argument('--headless')
driver = webdriver.Chrome(options=opts)

driver.get('https://www.cricbuzz.com/')
driver.maximize_window()
sleep(1)

print('Locators using ID')
aps_in=driver.find_element(By.ID,'apstag-init')
print('asp_in found')
gtm=driver.find_element(By.ID,'gtm')
print('gtm found')
leaderboard=driver.find_element(By.ID,'leaderboard')
print('leaderboard found')
goog_plcm_frame=driver.find_element(By.ID,'goog_plcm_frame')
print('goog_plcm_frame found')
clevertap_loader=driver.find_element(By.ID,'clevertap-loader')
print('clevertap_loader found')

print('Locators using NAME')
viewport=driver.find_element(By.NAME,'viewport')
print('viewport found')
robots=driver.find_element(By.NAME,'robots')
print('robots found')
googlebot=driver.find_element(By.NAME,'googlebot')
print('googlebot found')
twitter_img=driver.find_element(By.NAME,'twitter:image')
print('twitter image found')
twitter_card=driver.find_element(By.NAME,'twitter:card')
print('twitter card found')

print('Locators using CLASS')
#<div class="font-bold text-xl">Menu</div>
font_bold=driver.find_element(By.CLASS_NAME,'font-bold')
print('font_bold found')
mt=driver.find_elements(By.CLASS_NAME,'mt-6')
print('mt found')
print(len(mt))
mb=driver.find_elements(By.CLASS_NAME,'mb-3')
print('mb found')
print(len(mb))
my=driver.find_elements(By.CLASS_NAME,'my-2')
print('my found')
print(len(my))
footer=driver.find_element(By.CLASS_NAME,'page-wrapper')
print('footer found')








