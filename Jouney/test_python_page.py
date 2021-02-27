# -qUoAL4^H444
# E-5OERkSnnGz

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


capabilities = {
    "browserName": "chrome",
    "browserVersion": "75.0",
    "selenoid:options": {
        "enableVNC": True,
        # "enableVideo": False
    }
}


driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    
    desired_capabilities=capabilities)


def test_pyt():
    driver.get("http://www.python.org")
    
    assert "Python", driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    # driver.close()



# class PythonOrgSearch(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()

#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source


#     def tearDown(self):

# if __name__ == "__main__":
#     unittest.main()