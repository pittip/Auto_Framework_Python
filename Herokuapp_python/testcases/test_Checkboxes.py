import allure
import pytest

import conftest
from constants.locators import MainPage
from generic_app_functions.generics import navigate_to_page, validate_page_header


@pytest.fixture
def goToCheckboxesPage():
    navigate_to_page(MainPage.TO_CHECKBOXES_PAGE)


@allure.title('Verify that header contains text Checkboxes')
@allure.severity(allure.severity_level.MINOR)
def test_Checkboxes_header(goToCheckboxesPage):
    validate_page_header('Checkboxes')


@allure.title('Verify that there are 2 checkboxes present')
@allure.severity(allure.severity_level.BLOCKER)
def test_number_of_checkboxes(goToCheckboxesPage):
    assert len(conftest.driver.find_elements_by_xpath("//input[@type='checkbox']")) == 2


@allure.title('Verify that the 1st & 2nd checkboxes are unchecked and checked respectively by default')
@allure.severity(allure.severity_level.BLOCKER)
def test_default_state_of_checkboxes(goToCheckboxesPage):
    list_of_checkboxes = conftest.driver.find_elements_by_xpath("//input[@type='checkbox']")

    with allure.step('Verifying that the 1st checkbox is not set'):
        assert list_of_checkboxes[0].is_selected() is False

    with allure.step('Verifying that the 2nd checkbox is set'):
        assert list_of_checkboxes[1].is_selected() is True