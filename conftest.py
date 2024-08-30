import pytest
from selenium import webdriver
from iniconf.curl import base_page

@pytest.fixture(scope="function")
def start_from_login_page():
    driver = webdriver.Firefox()
    screen_width = driver.execute_script("return window.screen.width;")
    screen_height = driver.execute_script("return window.screen.height;")
    driver.set_window_size(screen_width, screen_height)
    driver.get(base_page)
    yield driver
    driver.quit()

