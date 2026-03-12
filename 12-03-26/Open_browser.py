##Open different browsers
from selenium import webdriver ##selenium package where collection of modules
from time import sleep  ##pause execution for certain time

##To Open Chrome browser
# driver= webdriver.Chrome()
# sleep(5) ##to close browser in 5 sec


##Open edge browser
# driver= webdriver.Edge()
# sleep(5)

##Open firefox
# driver= webdriver.Firefox() ##even if I do not have firefox it will still open
# sleep(5)


##if we do not want the browser to close automatically after 5sec using sleep
#using this we have to close it manually
# opts=webdriver.ChromeOptions() ##options tell use obout what configuration we want
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(options=opts)
#
# ##for edge browser
# opts1=webdriver.EdgeOptions()
# opts1.add_experimental_option("detach", True)
# # driver=webdriver.Edge(options=opts1)
#
# ##for firefox browser
# opts2=webdriver.FirefoxOptions()
# # opts2.add_argument('detach') ##in firefox add exp option is not there so we can use any of these two
# opts2.set_preference('detach', True)
# # driver=webdriver.Firefox(options=opts2)
#
# driver.get('https://supertails.com/') #open this website on chrome
# sleep(3)
##to maximize the whole window so that the elements do not overlap
# driver.maximize_window()
# sleep(2)

# driver.minimize_window()#to minimize the window
# sleep(3)

##to go back to the previous page
# driver.back()
# sleep(2)
# ##to go forward again
# driver.forward()
# sleep(2)
# ##to refresh the page
# driver.refresh()
# sleep(3)

##two methods close and quit
##close--> it closed the current not all window session keeps on running
##quit--> closes all the windows and the session ends
# driver.close()
# driver.quit()

##to print title name of url,link url and the name of browser
driver= webdriver.Chrome()
driver.get("https://www.supertails.com")
print(f'Title name: {driver.title}')
print(f'Link url: {driver.current_url}')
print(f'Browser name: {driver.name}')













