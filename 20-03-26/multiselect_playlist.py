from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get(r"C:\Users\agarw\OneDrive\Desktop\pycharm_project\Day-7_20-03-26\playlist.html")
driver.maximize_window()

songs_list=driver.find_element(By.ID,'songs')
select=Select(songs_list)

if select.is_multiple:
    select.select_by_index(6)
    select.select_by_visible_text('Wildest Dreams')
    select.select_by_visible_text('Cruel Summer')
    sleep(3)

print([i.text for i in select.all_selected_options])
print([i.text for i in select.options])
driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()

sleep(3)
driver.quit()
