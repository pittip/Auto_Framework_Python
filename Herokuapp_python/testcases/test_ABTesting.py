import allure
import pytest

import conftest
from constants.locators import MainPage
from generic_app_functions.generics import navigate_to_page

@pytest.fixture()
def goToABTestingPage():
    navigate_to_page(MainPage.TO_ABTESTING_PAGE)


@allure.title('Verify that header contains text A/B Test')
@allure.severity(allure.severity_level.MINOR)
def test_abTest_header(goToABTestingPage):
    with allure.step('Get the header text for validation'):
        a = conftest.driver.find_element_by_css_selector("h3").text

    with allure.step('Assert that header is correct'):
        assert 'A/B Test' in a


@allure.title('Verify the paragraph text to be as expected')
@allure.severity(allure.severity_level.CRITICAL)
def test_abTest_paragraph(goToABTestingPage):
    with allure.step('Get the paragraph text for validation'):
        a = conftest.driver.find_element_by_css_selector("p").text

    with allure.step('Assert that the paragraph content is as expected'):
        assert 'Also known as split testing. This is a way in which businesses are able to simultaneously test and learn ' \
           'different versions of a page to see which text and/or functionality works best towards a desired outcome ' \
           '(e.g. a user action such as a click-through).' == a