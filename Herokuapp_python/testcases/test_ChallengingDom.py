import allure
import pytest

import conftest
from constants.locators import MainPage
from generic_app_functions.generics import navigate_to_page, validate_page_header

@pytest.fixture
def goToChallengingDOMPage():
    navigate_to_page(MainPage.TO_CHALLENGING_DOM_PAGE)


@allure.title('Verify that header contains text Challenging DOM')
@allure.severity(allure.severity_level.MINOR)
def test_ChallengingDOMHeader(goToChallengingDOMPage):
    validate_page_header('Challenging DOM')


@allure.title('Verify the number of rows and columns in the table')
@allure.severity(allure.severity_level.CRITICAL)
def test_check_table_num_rows_num_cols(goToChallengingDOMPage):
    table = conftest.driver.find_element_by_css_selector("table > tbody")
    rows = table.find_elements_by_tag_name("tr")

    with allure.step('Verify the total number of rows is as expected'):
        assert len(rows) == 10

    cols = 0
    for row in rows:
        cols = row.find_elements_by_tag_name("td")
    else:
        with allure.step('Verify the total number of columns is as expected'):
            assert len(cols) == 7