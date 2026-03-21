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
select=Select(songs_list) ##it takes the dropdown only

if select.is_multiple:
    taylor_swift=driver.find_elements(By.XPATH, '//select[@id="songs"]/descendant::optgroup[4]/child::option')
    for song in taylor_swift:
        select.select_by_visible_text(song.text)

sleep(2)
print([i.text for i in select.all_selected_options])

driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()

sleep(2)
driver.quit()

