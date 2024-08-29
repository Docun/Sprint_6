import pytest
from selenium import webdriver
from iniconf.curl import base_page
from pages.base_click_logo import TestLogoNavigation


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def start_from_login_page(driver):
    driver.get(base_page)
    return driver