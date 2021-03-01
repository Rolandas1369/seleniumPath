from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


capabilities = {
    "browserName": "android",
    "browserVersion": "10.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
        

    }
}


driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",   
    desired_capabilities=capabilities)


def test_pyt1():

    print('Session ID is: %s' % driver.session_id)
    print('Opening the page...')
    driver.get("https://www.python.org/about/")
    
        
    elem = driver.find_element_by_name("q")
    elem.send_keys("selenium")
    elem.send_keys(Keys.RETURN)
    print('Typing search request...')
        
    assert driver.title != "Welcome to Python.org"
    print('Taking screenshot...')
    driver.get_screenshot_as_file('/home/rolandas/Desktop/PSel/Jouney/work/selenoid/video/' + driver.session_id + '.png')
    driver.quit()