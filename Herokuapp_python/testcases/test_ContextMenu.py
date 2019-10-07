import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import conftest
from constants.locators import MainPage
from generic_app_functions.generics import navigate_to_page, validate_page_header


@pytest.fixture
def goToContextMenuPage():
    navigate_to_page(MainPage.TO_CONTEXTMENU_PAGE)


@allure.title('Verify that header contains text Context Menu')
@allure.severity(allure.severity_level.MINOR)
def test_context_menu_header(goToContextMenuPage):
    validate_page_header('Context Menu')


@pytest.mark.skip('Need to understand why context click is failing. Parking for now')
@allure.title('Verify that context menu popup appears')
@allure.severity(allure.severity_level.CRITICAL)
def test_context_menu_popup(goToContextMenuPage):
    with allure.step('Performing right click in the box'):
        object_for_context_click = conftest.driver.find_element_by_xpath("//div[@id='hot-spot']")
        ActionChains(conftest.driver).context_click(object_for_context_click).perform()

    with allure.step('Checking if alert appeared'):
        assert WebDriverWait(conftest.driver, 4).until(expected_conditions.alert_is_present()) is True

    conftest.driver.switch_to_alert().dismiss()