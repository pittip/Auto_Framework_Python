import pytest

from constants.locators import MainPage
from generic_app_functions.generics import navigate_to_page, validate_page_header, validate_page_content_text


@pytest.fixture
def goToDisappearingElementsPage():
    navigate_to_page(MainPage.TO_DISAPPEARING_ELEMENTS_PAGE)

def test_disappearing_elements_header(goToDisappearingElementsPage):
    validate_page_header("Disappearing Elements")

def test_disappearing_elements_content(goToDisappearingElementsPage):
    validate_page_content_text("This example demonstrates when elements on a page change by disappearing/reappearing on each page load")