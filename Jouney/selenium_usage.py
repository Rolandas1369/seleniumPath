"""Add web driver"""
# Stored drivers in dependency, has many what to do if item(driver) not in list
# Remote driver gives access to remote sever
from selenium import webdriver
# Actions
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# doest wait for ajax
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
# remove prepopulated text field
elem.clear()
# type into field
elem.send_keys("pycon")
# Press enter ENTER == RETURN
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
# Close open driver, memory leaks?
driver.close()