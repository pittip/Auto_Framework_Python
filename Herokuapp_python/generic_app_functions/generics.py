import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import conftest

def validate_page_header(expected_page_header):
    with allure.step('Get the header text for validation'):
        a = WebDriverWait(conftest.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                                "h3"))).text

    with allure.step('Assert that the header is correct'):
        assert expected_page_header == a

def validate_page_content_text(expected_page_content_text):
    with allure.step('Get the page content text for validation'):
        a = WebDriverWait(conftest.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p"))).text

    with allure.step('Assert that the page text content is correct'):
        assert expected_page_content_text == a

def navigate_to_page(page_link_enum):
    with allure.step('Click on the link which navigates to the actual page'):
        WebDriverWait(conftest.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                          page_link_enum.value))).click()