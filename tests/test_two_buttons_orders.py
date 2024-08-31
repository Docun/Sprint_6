import allure
import pytest
from pages.orders_scooter import CheckOrderTwoButton
from locators.base_page_locators import MainPageLocators
from iniconf.data import personal_data_kit_first, personal_data_kit_second

class TestOrderScooter:
    @allure.title('Проверяем оформление заказа нажав по кнопке из шапки страницы')
    @allure.description('Заказываем самокат используя первый набор данных')
    @pytest.mark.parametrize('name, surname, address, phone_number, comment', [*personal_data_kit_first])
    def test_uno_order(self, start_from_login_page, name, surname, address, phone_number, comment):
        orders = CheckOrderTwoButton(start_from_login_page)
        orders.click_buttons_cockies()
        orders.click_button(MainPageLocators.ORDER_BUTTON)
        orders.order_collection(name, surname, address, phone_number, comment)
        order_text = orders.check_order_text()
        assert "Заказ оформлен" in order_text



    @allure.title('Проверяем оформление заказа нажав по кнопке из середины страницы')
    @allure.description('Заказываем самокат используя второй набор данных')
    @pytest.mark.parametrize('name, surname, address, phone_number, comment', [*personal_data_kit_second])
    def test_dos_order(self, start_from_login_page, name, surname, address, phone_number, comment):
        orders = CheckOrderTwoButton(start_from_login_page)
        orders.click_buttons_cockies()
        orders.scroll_and_click_button_order()
        orders.click_button(MainPageLocators.ORDER_BUTTON)
        orders.order_collection(name, surname, address, phone_number, comment)
        order_text = orders.check_order_text()
        assert "Заказ оформлен" in order_text




