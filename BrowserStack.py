#start BrowserStackLocal ./BrowserStackLocal MDKicy4nya2192zewKpz

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'browser': 'firefox', 'build': 'build1', 'browserstack.debug': 'true' }

driver = webdriver.Remote(
                          #command_executor='http://scottmaretick2:MDKicy4nya2192zewKpz@hub.browserstack.com:80/wd/hub',
                          command_executor='http://scottmaretick1:wWzHgVGrUqgDXdjZ5qKd@hub.browserstack.com:80/wd/hub',
                          desired_capabilities=desired_cap)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")

#driver.find_element_by_id("Email").clear()
#driver.find_element_by_id("Email").send_keys("scottmaretick51@gmail.com")
#driver.find_element_by_id("next").click()
#driver.find_element_by_id("Passwd-hidden").clear()
#driver.find_element_by_id("Passwd-hidden").send_keys("sm110751")
#driver.find_element_by_id("next").click()
#driver.find_element_by_link_text("Sign in").click()
#driver.find_element_by_link_text("Analytics").click()
print (driver.title) #need( ) for python3
driver.quit()
