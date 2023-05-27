import pytest
from selenium import webdriver

from data import Urls


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE_URL)
    yield driver

    driver.quit()
