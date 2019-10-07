import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import conftest
from constants.locators import MainPage
from generic_app_functions.generics import validate_page_header, navigate_to_page

@pytest.fixture
def goToAddRemoveElementsPage():
    navigate_to_page(MainPage.TO_ADD_REMOVE_ELEMENTS_PAGE)


@allure.title('Verify that header reads Add/Remove Elements')
@allure.severity(allure.severity_level.MINOR)
def test_AddRemoveHeader(goToAddRemoveElementsPage):
    validate_page_header('Add/Remove Elements')


@allure.title('Verify that Delete button is absent')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_button_absence(goToAddRemoveElementsPage):
    with allure.step('Assert that Delete button is absent'):
        assert len(conftest.driver.find_elements_by_xpath("//button[text()='Delete']")) == 0


@allure.title('Verify that Delete button is present when Add/Remove Elements button is clicked')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_button_presence_on_AddRemove_button_click(goToAddRemoveElementsPage):
    with allure.step('Click on Add/Remove Elements button'):
        WebDriverWait(conftest.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text("
                                                                                                   ")='Add "
                                                                                                   "Element']"))).click()

    with allure.step('Assert that Delete but appears'):
        assert WebDriverWait(conftest.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                                "//button[text("
                                                                                                ")='Delete']"))).is_displayed() is True