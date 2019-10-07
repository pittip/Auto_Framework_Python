import allure
import pytest
import requests

from constants.locators import MainPage
from generic_app_functions.generics import validate_page_header, navigate_to_page

@pytest.fixture()
def goToBrokenImagesPage():
    navigate_to_page(MainPage.TO_BROKEN_IMAGES_PAGE)


@allure.title('Verify that header contains text Broken Images')
@allure.severity(allure.severity_level.MINOR)
def test_BrokenImages_header(goToBrokenImagesPage):
    validate_page_header('Broken Images')


@allure.title('Verify images for broken links')
@allure.severity(allure.severity_level.CRITICAL)
def test_images_for_broken_links(goToBrokenImagesPage):
    r = requests.get('http://the-internet.herokuapp.com/asdf.jpg')
    with allure.step('Verify 1st image has a broken image link'):
        assert r.status_code == 404

    r = requests.get('http://the-internet.herokuapp.com/hjkl.jpg')
    with allure.step('Verify 2nd image has a broken image link'):
        assert r.status_code == 404

    r = requests.get('http://the-internet.herokuapp.com/img/avatar-blank.jpg')
    with allure.step('Verify 3rd image does not have a broken image link'):
        assert r.status_code == 200