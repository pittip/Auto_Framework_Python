import allure
import pytest

import conftest
from generic_app_functions.generics import validate_page_header

@pytest.fixture
def goToBasicAuthPage():
    conftest.driver.get('http://admin:admin@the-internet.herokuapp.com/')


@allure.title('Verify that header contains text Basic Auth')
@allure.severity(allure.severity_level.MINOR)
def test_BasicAuthHeader(goToBasicAuthPage):
    validate_page_header('Basic Auth')


@pytest.mark.skip(reason = 'Not sure how to automate it')
@allure.title('Verify that user is successfully authenticated')
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_authentication(goToBasicAuthPage):
    with allure.step('Get the paragraph text for validation'):
        a = conftest.driver.find_element_by_css_selector("p").text

    with allure.step('Assert that the paragraph content is as expected'):
        assert 'Congratulations! You must have the proper credentials.' == a