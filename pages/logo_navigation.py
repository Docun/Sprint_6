from locators.logo_header_locators import LocatorsLogo
from locators.orders_scooter_locators import LocatorsOrder
from pages.base_page import BasePage
from iniconf.curl import *
import allure

class TestLogoNavigation(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.yandex_logo = LocatorsLogo.yandex_logo
        self.scooter_logo = LocatorsLogo.scooter_logo
        self.order_button = LocatorsOrder.order_button


    def open_new_page(self):
        self.close_and_open_new_page()

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_yandex_logo(self):
        self.wait_for_element_visibility(self.yandex_logo)

    @allure.step('Кликаем на лого яндекса')
    def click_by_logo_yandex(self):
        self.click_button(self.yandex_logo)

    @allure.step('Ждем загрузки новой страницы и проверяем что открылся дзен')
    def wait_for_navigation_to_dzen(self):
        self.wait_for_number_of_windows(2, base_dzen)

    @allure.step('Проверяем что страница открылась')
    def wait_for_load_scooter_logo(self):
        self.wait_for_element_visibility(self.scooter_logo)

    @allure.step('Кликаем по кнопке заказать')
    def click_by_button_order(self):
        self.click_button(self.order_button)

    @allure.step('Кликаем по кнопке лого самоката')
    def click_by_logo_scooter(self):
        self.click_button(self.scooter_logo)

    @allure.step('Ждем нужный URL для начальной страницы')
    def wait_navigation_base_page(self):
        self.wait_for_url_contains(base_page)

    @allure.step('Проверяем URL, должны остаться на главной странице')
    def check_url_base_page(self):
        self.check_text(base_page)