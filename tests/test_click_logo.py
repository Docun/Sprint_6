from pages.base_click_logo import ClickYandexLogo, ClickScootersLogo
from iniconf.curl import base_page
import pytest
import allure

base_url = base_page


class TestYandexLogo:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = ClickYandexLogo(start_from_login_page)

    def test_yandex_logo_navigation(self):
        self.page.wait_for_load_logo()
        self.page.click_by_logo_yandex()
        self.page.wait_for_navigation()


class TestScootersLogo:
    @pytest.fixture(autouse=True)
    def setup(self, start_from_login_page):
        self.page = ClickScootersLogo(start_from_login_page)

    def test_scooter_logo_navigation(self):
        self.page.wait_for_load_logo()  # ждем загрузки логотипа
        self.page.click_by_button_order()  # кликаем на кнопку заказа
        self.page.click_by_logo_scooter()  # кликаем на логотип самоката
        self.page.wait_navigation_base_page()  # ждем загрузки нужного URL
        self.page.check_url_bu()  # сравниваем URL
