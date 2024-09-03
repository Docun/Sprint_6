from locators.logo_locators import LocatorsLogo
from locators.base_page_locators import MainPageLocators
from pages.base_page import BasePage
from iniconf.curl import *
import allure


class TestLogoNavigation(BasePage):
    @allure.step('Кликаем на лого яндекса')
    def click_by_logo_yandex(self):
        self.click_button(LocatorsLogo.YANDEX_LOGO)

    @allure.step('Кликаем по кнопке лого самоката')
    def click_by_logo_scooter(self):
        self.click_button(LocatorsLogo.SCOOTER_LOGO)

    @allure.step('Кликаем по кнопке заказать')
    def click_by_button_order(self):
        self.click_button(MainPageLocators.ORDER_BUTTON)

    @allure.step('Ждем загрузки новой страницы и проверяем что открылся дзен')
    def wait_for_navigation_to_dzen(self):
        self.wait_for_number_of_windows(2, base_dzen)

    @allure.step('Проверяем URL, должны остаться на главной странице')
    def check_url_base_page(self):
        self.verify_current_url(base_page)
