import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = None

@pytest.fixture(autouse = True)
def browserSetAndClose():
    global driver

    EXE_PATH = r'E:\Software setups\selenium_browser_drivers\chromedriver.exe'
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(executable_path = EXE_PATH, options = chromeOptions, desired_capabilities =
     chromeOptions.to_capabilities())
    driver.implicitly_wait(5)
    driver.maximize_window()

    with allure.step('Launch the application'):
        driver.get('http://the-internet.herokuapp.com/')

    yield driver
    with allure.step('Close the application'):
        driver.quit()