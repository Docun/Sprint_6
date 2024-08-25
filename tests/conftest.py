import pytest
from selenium import webdriver



@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def start_from_login_page(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    return driver

