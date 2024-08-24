from locators.logo_page import LocatorsLogo
from locators.orders_scooter import LocatorsOrder
from test_base import BasePage
from iniconf.curl import *


# Класс для проверки перехода по логу Яндекса на Дзен
class ClickYandexLogo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.yandex_logo = LocatorsLogo.yandex_logo

    def wait_for_load_logo(self):
        self.wait_for_element_visibility(self.yandex_logo)

    def click_by_logo_yandex(self):
        self.click_button(self.yandex_logo)

    def wait_for_navigation(self):
        self.wait_for_number_of_windows(2)



# Класс для проверки перехода по логу самоката на страницу самоката
class ClickScootersLogo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.scooter_logo = LocatorsLogo.scooter_logo
        self.order_button = LocatorsOrder.order_button

    def wait_for_load_logo(self):
        self.wait_for_element_visibility(self.scooter_logo)

    def click_by_button_order(self):
        self.driver.find_element(*self.order_button).click()

    def click_by_logo_scooter(self):
        self.driver.find_element(*self.scooter_logo).click()

    # перепроверить assert
    def wait_navigation_base_page(self):
        self.wait_for_url_contains(base_page)
